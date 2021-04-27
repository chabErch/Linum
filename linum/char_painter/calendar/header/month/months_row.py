from datetime import date
from typing import List, Any

from linum.char_painter.base import DateRow
from linum.helper import split_by_months
from .month_cell import MonthCell


class MonthsRow(DateRow):

    def __init__(self, start_date: date = date.today(), length: int = 0):
        """
        Строка с названиями месяцев.

        :param start_date: начальная дата
        :param length: период отображения
        """
        super().__init__(start_date, length)

    def __repr__(self):
        return "<MonthRow at {} with length {}>".format(self.start_date, self.length)

    @property
    def cells(self) -> List[MonthCell]:
        """
        Пререндер строки с названиями месяцев.
        Возвращает список с ячейками — названиями месяцев.

        :return: List[MonthCell]
        """
        if self.length == 0:
            return []

        cells = []

        months = split_by_months(self.start_date, self.length)
        for d, length in months:
            cell_width = length * self.cell_width
            cell_width += length - 1 if self.inner_borders else 0
            mc = MonthCell(cell_width, d)
            cells.append(mc)

        if self.inner_borders:
            cells = self.set_month_borders(cells, self.inner_border_char)

        if self.month_inner_borders:
            cells = self.set_month_borders(cells, self.month_inner_border_char)

        return cells

    @cells.setter
    def cells(self, any_: Any):
        """
        Заглушка. Не вносит никаких изменений.
        Необходима для корректного вызова конструктора родительского класса.

        :param any_:
        """
        pass

    # def render(self) -> str:
    #     """
    #     Рендер строки с названиями месяцев
    #
    #     :return:
    #     """
    #     cells = self.cells
    #     row = Row(cells)
    #
    #     # Выставляем левую границу
    #     row.left_border = self.left_border
    #     row.left_border_char = self.left_border_char
    #
    #     # Выставляем правую границу
    #     row.right_border = self.right_border
    #     row.right_border_char = self.right_border_char
    #
    #     # Выставляем внутренние границы
    #     row.inner_borders = self.month_inner_border or self.inner_borders
    #     row.inner_border_char = self.month_inner_border_char
    #
    #     return row.render()
