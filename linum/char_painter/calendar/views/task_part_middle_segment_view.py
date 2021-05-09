from linum import TaskPart
from linum.char_painter.base.cell import Cell
from linum.char_painter.base.date_row import DateRow
from linum.char_painter.enums import Align


class TaskPartMiddleSegmentView(DateRow):

    def __init__(self, task_part: TaskPart):
        """
        Представление кусочка задачи.

        :param task_part: кусочек задачи
        """
        self.task_part = task_part
        super().__init__(task_part.start, task_part.length)

    def pre_render(self, *args) -> Cell:
        """
        Возвращает средний сегмент в виде ячейки.

        :return: Cell
        """
        cell = super().pre_render()
        cell.content = self.task_part.task.name
        cell.right_border = True
        cell.left_border = True
        cell.align = Align.LEFT
        if not self.inner_borders:
            cell.cell_width -= 2
            content = cell.render()
            cell = Cell(len(content), content)

        return cell
