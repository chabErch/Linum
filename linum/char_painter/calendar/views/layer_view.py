from datetime import date, timedelta
from typing import List

from linum import Layer
from linum.char_painter.base import Border
from linum.char_painter.base import Cell
from linum.char_painter.base import Row
from linum.char_painter.calendar.grid import GridCell
from linum.char_painter.calendar.grid import GridRow
from linum.char_painter.calendar.space import SpaceRow
from .task_part_view import TaskPartView


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
        self.month_inner_borders = True

        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)
        self.month_inner_border_char = Border(t=True, b=True)

    def pre_render_middle_segment(self) -> Cell:
        layer = self._trim_layer(self.start_date, self.length)

        row = Row()
        previous_date = self.start_date

        for part in layer.parts:
            # Создаем ячейки между текущей и предыдущей задачами
            count = (part.start - previous_date).days
            sr = SpaceRow(previous_date, count)
            sr.cell_width = self.cell_width
            sr.month_inner_borders = self.month_inner_borders
            sr.inner_borders = self.inner_borders
            if (not self.inner_borders and self.month_inner_borders) or sr.pre_render().cell_width > 0:
                row.append(sr.pre_render())

            # Создаем ячейку потока слиянием нескольких ячеек
            tpv = TaskPartView(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders
            tpv.month_inner_borders = self.month_inner_borders
            row.append(tpv.pre_render_middle_segment())

            previous_date = part.day_after

        # Создаем пустые ячейки после последней задачи
        if previous_date < self.start_date + timedelta(self.length):
            count = (self.start_date + timedelta(self.length) - previous_date).days
            sr = SpaceRow(previous_date, count)
            sr.cell_width = self.cell_width
            sr.month_inner_borders = self.month_inner_borders
            sr.inner_borders = self.inner_borders
            row.append(sr.pre_render())

        row.left_border = self.left_border
        row.left_border_char = self.left_border_char
        row.right_border = self.right_border
        row.right_border_char = self.right_border_char

        return row.merge()

    def render_middle_segment(self) -> str:
        """
        Возвращает средний сегмент слоя с кусочками задач за указанный период.

        :return: str
        """
        cell = self.pre_render_middle_segment()
        return cell.render()

    def pre_render_outline(self, is_top_outline=True) -> Cell:
        layer = self._trim_layer(self.start_date, self.length)

        row = Row()
        previous_date = self.start_date

        for part in layer.parts:
            # Создаем ячейки между текущей и предыдущей задачами
            count = (part.start - previous_date).days
            sr = SpaceRow(previous_date, count)
            sr.cell_width = self.cell_width
            sr.month_inner_borders = self.month_inner_borders
            sr.inner_borders = self.inner_borders
            if (not self.inner_borders and self.month_inner_borders) or sr.pre_render().cell_width > 0:
                row.append(sr.pre_render())

            # Создаем ячейку потока слиянием нескольких ячеек
            tpv = TaskPartView(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders
            tpv.month_inner_borders = self.month_inner_borders
            row.append(tpv.pre_render_outline(is_top_outline))

            previous_date = part.day_after

        # Создаем пустые ячейки после последней задачи
        if previous_date < self.start_date + timedelta(self.length):
            count = (self.start_date + timedelta(self.length) - previous_date).days
            sr = SpaceRow(previous_date, count)
            sr.cell_width = self.cell_width
            sr.month_inner_borders = self.month_inner_borders
            sr.inner_borders = self.inner_borders
            row.append(sr.pre_render())

        row.left_border = self.left_border
        row.left_border_char = self.left_border_char
        row.right_border = self.right_border
        row.right_border_char = self.right_border_char

        return row.merge()

    def render_outline(self, is_top_outline=True) -> str:
        cell = self.pre_render_outline(is_top_outline)
        return cell.render()

    def get_outline(self, is_top_outline: bool = True) -> str:
        """
        Возвращает строковое представление верхнего или нижнего сегмента слоя.

        :param is_top_outline:
        :return:
        """
        layer = self._trim_layer(self.start_date, self.length)

        grid_row = GridRow()
        previous_date = self.start_date
        part = None

        for part in layer.parts:
            # Создаем ячейки между текущей и предыдущей задачами
            count = (part.start - previous_date).days
            pre_cells = self._get_empty_grid_cells(count)
            grid_row.append(pre_cells)

            previous_date = part.day_after

            # Формируем представление кусочка задачи
            tpv = TaskPartView(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders

            # Создаем ячейки над задачей
            part_cell = tpv.pre_render_outline(is_top_outline)
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

    def _trim_layer(self, start_date: date, length: int) -> Layer:
        """
        Обрезает части слоя, находящиеся вне заданного периода отображения.

        :return: Layer
        """
        _, layer = self.layer.split(start_date)
        layer, _ = layer.split(start_date + timedelta(length))
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
