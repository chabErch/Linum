import os
from copy import copy
from typing import List, Optional

import yamale

from linum import Task
from linum.color import Color
from linum.context import CharPainterContext, ExcelRendererContext
from linum.excel_renderer.base.style import Style

DATA_SCHEMA_PATH = os.path.dirname(__file__) + "/data_schema.yaml"
CONTEXT_SCHEMA_PATH = os.path.dirname(__file__) + "/context_schema.yaml"


class Loader:

    def __init__(self):
        """ Загрузчик задач и настроек визуализации из yaml файла. """
        pass

    def load_tasks(self, yaml_path: Optional[str] = None) -> List[Task]:
        """
        Загружает задачи, указанные в yaml файле

        :param yaml_path: путь до yaml файла
        :return: List[Task]
        """
        if not yaml_path:
            return []

        # Загружаем схему
        schema = yamale.make_schema(DATA_SCHEMA_PATH)
        # Загружаем данные
        data = yamale.make_data(yaml_path)
        # Валидируем
        yamale.validate(schema, data)
        # Загружаем задачи
        tasks = self._data_to_tasks(data[0][0])
        return tasks

    @staticmethod
    def load_char_painter_context(yaml_path: Optional[str] = None) -> CharPainterContext:
        """
        Загружает контекст из указанного файла.

        :param yaml_path: путь к файлу
        :return: CharPainterContext
        """
        if not yaml_path:
            return CharPainterContext()

        # Загружаем схему
        schema = yamale.make_schema(CONTEXT_SCHEMA_PATH)
        # Загружаем данные
        data = yamale.make_data(yaml_path)
        # Валидируем
        yamale.validate(schema, data)
        # Загружаем данные
        base_data = data[0][0].get('base', {})
        char_painter_data = data[0][0].get('char_painter', {})
        base_data.update(char_painter_data)
        # Формируем контекст
        cpc = CharPainterContext(**base_data)
        return cpc

    def _data_to_tasks(self, data: dict) -> List[Task]:
        tasks = []
        for k, v in data.items():
            tasks += self._recursive_task_load(Task(k), v)
        return tasks

    def _recursive_task_load(self, task: Task, data: dict) -> List[Task]:
        start_date = data.get('date')
        task.start_date = start_date if start_date else task.start_date

        length = data.get('length')
        task.length = length if length else task.length

        finish = data.get('finish')
        task.length = (finish - start_date).days if finish else task.length

        color = data.get('color')
        task.color = color if color else Color.get_random_rgb()

        if 'sub' not in data:
            return [task]
        elif isinstance(data['sub'], dict):
            tasks = []
            for k, v in data['sub'].items():
                task_ = copy(task)
                task_.name += str(k)
                tasks += self._recursive_task_load(task_, v)
            return tasks
        elif isinstance(data['sub'], list):
            tasks = []
            for v in data['sub']:
                task_ = copy(task)
                tasks += self._recursive_task_load(task_, v)
            return tasks

    @staticmethod
    def load_excel_renderer_context(yaml_path: Optional[str] = None) -> ExcelRendererContext:
        # Upload schema
        schema = yamale.make_schema(CONTEXT_SCHEMA_PATH)
        # Upload all data
        data = yamale.make_data(yaml_path)
        # Validating
        yamale.validate(schema, data)
        data = data[0][0]

        days_off_list = data.pop("days_off", [])
        workdays_list = data.pop("workdays", [])

        # ====================================================================

        def _recursive(d: dict) -> Style:
            style = Style(**d)
            for k, v in style.items():
                if isinstance(v, dict):
                    s = _recursive(v)
                    s.parents = [style]
                    style.update({k: s})
            return style

        excel_renderer = data.pop("excel_renderer", {})
        styles = _recursive(excel_renderer.pop("styles", {}))

        # ====================================================================

        kwargs = {}
        kwargs.update(data.get("period", {}))
        kwargs.update(excel_renderer)
        kwargs.update({"styles": styles, "days_off": days_off_list, "workdays": workdays_list})
        return ExcelRendererContext(**kwargs)
