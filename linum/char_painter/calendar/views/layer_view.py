from datetime import date, timedelta
from typing import List

from linum import Layer
from linum.char_painter.base import Border
from linum.char_painter.base import Cell
from linum.char_painter.base import Row
from linum.char_painter.calendar.grid import GridCell
from linum.char_painter.calendar.grid import GridRow
from linum.char_painter.calendar.space import SpaceRow
from .task_part_middle_segment_view import TaskPartMiddleSegmentView
from .task_part_outline_view import TaskPartOutlineView


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
        cell = self._pre_render_segment(TaskPartMiddleSegmentView)
        return cell

    def render_middle_segment(self) -> str:
        """
        Возвращает средний сегмент слоя с кусочками задач за указанный период.

        :return: str
        """
        cell = self.pre_render_middle_segment()
        return cell.render()

    def pre_render_outline(self, is_top_outline=True) -> Cell:
        cell = self._pre_render_segment(TaskPartOutlineView, is_top_outline)
        return cell

    def render_outline(self, is_top_outline=True) -> str:
        cell = self.pre_render_outline(is_top_outline)
        return cell.render()

    def _pre_render_segment(self, segment_class, is_top_outline: bool = True) -> Cell:
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
            cell = sr.pre_render()
            if not self.inner_borders and self.month_inner_borders and previous_date.day == 1:
                content = cell.render()
                cell = Cell(len(content), content)
                cell.left_border = True
            if sr:
                row.append(cell)

            # Создаем ячейку потока слиянием нескольких ячеек
            tpv = segment_class(part)
            tpv.cell_width = self.cell_width
            tpv.inner_borders = self.inner_borders
            tpv.month_inner_borders = self.month_inner_borders
            cell = tpv.pre_render(is_top_outline)
            if not self.inner_borders and self.month_inner_borders and part.start.day == 1:
                content = cell.render()
                cell = Cell(len(content), content)
                cell.left_border = True
            row.append(cell)

            previous_date = part.day_after

        # Создаем пустые ячейки после последней задачи
        if previous_date < self.start_date + timedelta(self.length):
            count = (self.start_date + timedelta(self.length) - previous_date).days
            sr = SpaceRow(previous_date, count)
            sr.cell_width = self.cell_width
            sr.month_inner_borders = self.month_inner_borders
            sr.inner_borders = self.inner_borders
            cell = sr.pre_render()
            if not self.inner_borders and self.month_inner_borders and previous_date.day == 1:
                content = cell.render()
                cell = Cell(len(content), content)
                cell.left_border = True
            row.append(cell)

        row.left_border = self.left_border
        row.left_border_char = self.left_border_char
        row.right_border = self.right_border
        row.right_border_char = self.right_border_char
        if len(row.cells) > 0:
            row.cells[0].left_border = self.left_border
            row.cells[-1].right_border = self.right_border

        return row.merge()

    def _trim_layer(self, start_date: date, length: int) -> Layer:
        """
        Обрезает части слоя, находящиеся вне заданного периода отображения.

        :return: Layer
        """
        _, layer = self.layer.split(start_date)
        layer, _ = layer.split(start_date + timedelta(length))
        return layer
