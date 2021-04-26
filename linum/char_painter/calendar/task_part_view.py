from copy import copy

from linum.char_painter.base.border import Border
from linum.char_painter.base.cell import Cell
from linum.char_painter.base.date_row import DateRow
from linum.char_painter.base.row import Row
from linum.char_painter.enums import Align
from linum.char_painter.grid.grid_cell import GridCell
from linum.char_painter.grid.grid_row import GridRow
from linum.task_part import TaskPart


class TaskPartView(DateRow):

    def __init__(self, task_part: TaskPart):
        """
        Представление кусочка задачи.

        :param task_part: кусочек задачи
        """
        self.task_part = task_part
        super().__init__(task_part.start_date, task_part.length)

    def pre_render_middle_segment(self) -> Cell:
        """
        Возвращает средний сегмент в виде ячейки.

        :return: Cell
        """
        cell = self.merge(self.task_part.task.name)
        cell.right_border = True
        cell.left_border = True
        cell.align = Align.LEFT
        if not self.inner_borders:
            cell.cell_width -= 2
            content = cell.render()
            cell = Cell(len(content), content)

        return cell

    def get_outline_cell(self, is_top_outline=True) -> GridCell:
        """
        Возвращает строковое представление верхнего или нижнего сегмента кусочка задачи.

        :param is_top_outline: верхняя или нижняя часть
        :return: GridCell
        """
        # Подготавливаем шаблонную ячейку для заполнения ею строки
        c = GridCell(self.cell_width)
        c.fill_char = Border(l=True, r=True)

        # Заполняем строку шаблонными ячейками
        part_row = GridRow([copy(c) for _ in range(self.task_part.length)])

        # Устанавливаем внутренние границы
        inner_border_char = Border(t=is_top_outline, b=not is_top_outline, l=True, r=True)
        part_row.inner_borders = self.inner_borders
        part_row.inner_border_char = inner_border_char

        # Устанавливаем левую границу
        part_row.left_border = True
        part_row.left_border_char = Border(t=True, r=True, b=True)

        # Устанавливаем правую границу
        part_row.right_border = True
        part_row.right_border_char = Border(t=True, l=True, b=True)

        # Сливаем строку в одну ячейку
        part_cell = part_row.merge()

        # Имитируем границу задачи если границы не рисуются сами
        if not self.inner_borders and part_cell.cell_width > 0:
            part_cell.content[0] -= Border(l=True)
            part_cell.content[0] += Border(b=is_top_outline, t=not is_top_outline)
            part_cell.content[-1] -= Border(r=True)
            part_cell.content[-1] += Border(b=is_top_outline, t=not is_top_outline)

        return part_cell
