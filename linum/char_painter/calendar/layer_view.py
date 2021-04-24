from datetime import date, timedelta
from typing import List

from linum.char_painter.base.border import Border
from linum.char_painter.base.cell import Cell
from linum.char_painter.base.row import Row
from linum.char_painter.calendar.task_part_view import TaskPartView
from linum.char_painter.grid.grid_cell import GridCell
from linum.char_painter.grid.grid_row import GridRow
from linum.layer import Layer


class LayerView:

    def __init__(self, layer: Layer, start_date: date = date.today(), length: int = 0):
        """
        Представление слоя с кусочками задач.

        :param layer: слой для представления
        :param start_date: начальная дата отображения
        :param length: продолжительность отображения
        """
        self.layer = layer
        self.length = length
        self.start_date = start_date

        self.cell_width = 4

        self.left_border = False
        self.right_border = False
        self.inner_borders = False

        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)

    def get_middle_segment(self) -> str:
        """
        Возвращает средний сегмент слоя с кусочками задач.

        :return: str
        """
        layer = self._trim_layer()

        row = Row()
        previous_date = self.start_date
        part = None

        for part in layer.parts:
            # Создаем ячейки между текущей и предыдущей задачами
            count = (part.start_date - previous_date).days
            row.append(self._get_empty_cells(count))

            previous_date = part.day_after

            # Создаем ячейку потока слиянием нескольких ячеек
            tpv = TaskPartView(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders
            row.append(tpv.as_cell())

        # Создаем пустые ячейки после последней задачи
        if part:
            count = (self.start_date + timedelta(self.length) - part.day_after).days
            post_cells = self._get_empty_cells(count)
            row.append(post_cells)

        # Выставляем внутренние границы
        row.inner_borders = self.inner_borders
        row.inner_border_char = self.inner_border_char

        # Выставляем левую границу
        row.left_border = self.left_border
        row.left_border_char = self.left_border_char

        # Выставляем правую границу
        row.right_border = self.right_border
        row.right_border_char = self.right_border_char

        return row.render()

    def get_outline(self, is_top_outline: bool = True) -> str:
        """
        Возвращает строковое представление верхнего или нижнего сегмента слоя.

        :param is_top_outline:
        :return:
        """
        layer = self._trim_layer()

        grid_row = GridRow()
        previous_date = self.start_date
        part = None

        for part in layer.parts:
            # Создаем ячейки между текущей и предыдущей задачами
            count = (part.start_date - previous_date).days
            pre_cells = self._get_empty_grid_cells(count)
            grid_row.append(pre_cells)

            previous_date = part.day_after

            # Формируем представление кусочка задачи
            tpv = TaskPartView(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders

            # Создаем ячейки над задачей
            part_cell = tpv.get_outline_cell(is_top_outline)
            grid_row.append(part_cell)

        # Создаем пустые ячейки после последней задачи
        if part:
            count = (self.start_date + timedelta(self.length) - part.day_after).days
            post_cells = self._get_empty_grid_cells(count)
            grid_row.append(post_cells)

        # Устанавливаем внутренние границы
        grid_row.inner_borders = self.inner_borders
        grid_row.inner_border_char = self.inner_border_char

        # Устанавливаем левую границу
        grid_row.left_border = self.left_border
        grid_row.left_border_char = self.left_border_char

        # Устанавливаем правую границу
        grid_row.right_border = self.right_border
        grid_row.right_border_char = self.right_border_char

        return grid_row.render()

    def _trim_layer(self) -> Layer:
        """
        Обрезает части слоя, находящиеся вне заданного периода отображения.

        :return: Layer
        """
        _, layer = self.layer.split(self.start_date)
        layer, _ = layer.split(self.start_date + timedelta(self.length))
        return layer

    def _get_empty_cells(self, count: int) -> List[Cell]:
        """
        Функция размножения пустых ячеек

        :param count: количество необходимых ячеек
        :return: List[Cell]
        """
        cells = [Cell(self.cell_width) for _ in range(count)]
        return cells

    def _get_empty_grid_cells(self, count: int) -> List[GridCell]:
        """
        Функция размножения пустых граничных ячеек

        :param count: количество необходимых ячеек
        :return: List[GridCell]
        """
        cells = [GridCell(self.cell_width) for _ in range(count)]
        return cells
