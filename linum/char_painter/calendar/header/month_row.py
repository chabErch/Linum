from datetime import date, timedelta
from typing import List

from linum.char_painter.base.border import Border
from linum.char_painter.base.row import Row
from linum.char_painter.calendar.header.month_cell import MonthCell


class MonthRow:

    def __init__(self, start_date: date = date.today(), length: int = 0):
        """
        Строка с названиями месяцев.

        :param start_date: начальная дата
        :param length: период отображения
        """
        self.start_date = start_date
        self.length = length

        self.cell_width = 4

        self.left_border = False
        self.right_border = False
        self.inner_borders = False
        self.month_inner_border = False

        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.month_inner_border_char = Border(t=True, b=True)

    def __repr__(self):
        return "<MonthRow at {} with length {}>".format(self.start_date, self.length)

    def pre_render(self) -> List[MonthCell]:
        """
        Пререндер строки с названиями месяцев.
        Возвращает список с ячейками — названиями месяцев.

        :return: List[MonthCell]
        """
        if self.length == 0:
            return []

        days_count = 0
        month_cells = []
        d = self.start_date

        # Проходим по всем дням из периода отображения
        for i in range(self.length):

            # Выставляем границу между соседними датами разных месяцев
            if (d + timedelta(days_count)).day == 1 and days_count > 0:
                mc_width = days_count * self.cell_width
                mc_width = mc_width + (days_count - 1) if self.inner_borders else mc_width

                mc = MonthCell(mc_width, d)
                month_cells.append(mc)

                d = self.start_date + timedelta(i)
                days_count = 1
            else:
                days_count += 1

        # Корректируем первый день последнего месяца
        # if d.day == 1 and days_count == 0:
        #     days_count += 1

        # Выставляем границу между последним и предпоследним месяцами
        mc_width = self.cell_width * days_count
        mc_width = mc_width + days_count - 1 if self.inner_borders else mc_width

        mc = MonthCell(mc_width, d)
        month_cells.append(mc)

        return month_cells

    def render(self) -> str:
        """
        Рендер строки с названиями месяцев

        :return:
        """
        cells = self.pre_render()
        row = Row(cells)

        # Выставляем левую границу
        row.left_border = self.left_border
        row.left_border_char = self.left_border_char

        # Выставляем правую границу
        row.right_border = self.right_border
        row.right_border_char = self.right_border_char

        # Выставляем внутренние границы
        row.inner_borders = self.month_inner_border or self.inner_borders
        row.inner_border_char = self.month_inner_border_char

        return row.render()
