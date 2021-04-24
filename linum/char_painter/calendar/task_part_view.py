from copy import copy

from linum.char_painter.base.border import Border
from linum.char_painter.base.cell import Cell
from linum.char_painter.base.row import Row
from linum.char_painter.enums import Align
from linum.char_painter.grid.grid_cell import GridCell
from linum.char_painter.grid.grid_row import GridRow
from linum.task_part import TaskPart


class TaskPartView:

    def __init__(self, task_part: TaskPart):
        """
        Представление среднего сегмента кусочка задачи.

        :param task_part: кусочек задачи
        """
        self.task_part = task_part

        self.cell_width = 4
        self.inner_borders = False

    def as_cell(self) -> Cell:
        """
        Возвращает средний сегмент в виде ячейки.

        :return: Cell
        """
        # Создаем строку из нужного количества ячеек
        part_row = Row([Cell(self.cell_width)] * self.task_part.length)

        # Учитываем внутренние границы
        part_row.inner_borders = self.inner_borders

        # Сливаем строку в одну ячейку
        part_cell = part_row.merge(self.task_part.task.name, Align.LEFT)

        # Имитируем границы ячейки
        if not self.inner_borders:
            part_cell.left_border = True
            part_cell.right_border = True
            part_cell.cell_width -= 2

        return part_cell

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
