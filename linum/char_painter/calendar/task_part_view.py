from linum.char_painter.base.border import Border
from linum.char_painter.base.cell import Cell
from linum.char_painter.base.date_row import DateRow
from linum.char_painter.calendar.grid import GridRow
from linum.char_painter.enums import Align
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

    def pre_render_outline(self, is_top_outline=True) -> Cell:
        """
        Возвращает строковое представление верхнего или нижнего сегмента кусочка задачи.

        :param is_top_outline: верхняя или нижняя часть
        :return: GridCell
        """
        gr = GridRow(self.start_date, self.length, is_top_outline)
        gr.cell_width = self.cell_width
        gr.inner_borders = self.inner_borders
        gr.left_border = True
        gr.right_border = True
        cell = gr.merge()
        if self.inner_borders:
            cell.left_border_char += Border(t=is_top_outline, b=not is_top_outline)
            cell.right_border_char += Border(t=is_top_outline, b=not is_top_outline)
        if not self.inner_borders:
            cell.content = cell.content[:-2]
            cell.cell_width -= 2
            content = cell.render()
            cell = Cell(len(content), content)

        return cell
