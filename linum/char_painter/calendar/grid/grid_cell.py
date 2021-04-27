from datetime import date
from typing import Any

from linum.char_painter.base import Border
from linum.char_painter.base import DateCell


class GridCell(DateCell):

    def __init__(self, cell_width: int = 0, date_: date = date.today):
        """
        Сеточная ячейка. Нужна для рисования сеток.

        :param cell_width: ширина ячейки в символах
        :param date_: дата ячейки
        """
        super().__init__(cell_width, date_)
        self.left_border_char = Border(r=True)
        self.right_border_char = Border(l=True)
        self.fill_char = Border(l=True, r=True)

    @property
    def content(self) -> str:
        return self.cell_width * str(self.fill_char)

    @content.setter
    def content(self, value: Any):
        pass
