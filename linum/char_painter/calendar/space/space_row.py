from datetime import date

from linum.char_painter.base.cell import Cell
from linum.char_painter.base.date_row import DateRow
from linum.char_painter.calendar.space.space_cell import SpaceCell


class SpaceRow(DateRow):

    def __init__(self, start_date: date, length: int):
        super().__init__(start_date, length)

    def pre_render(self) -> Cell:
        cell = super().pre_render()
        if self.start_date.day == 1:
            cell.left_border = True
        return cell

    @property
    def date_cell_class(self):
        return SpaceCell



