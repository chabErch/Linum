from datetime import date

from linum.char_painter.base.border import Border
from linum.char_painter.calendar.header.days_row import DaysRow
from linum.char_painter.calendar.header.month_row import MonthRow
from linum.char_painter.calendar.header.weekdays_row import WeekdaysRow


class Header:

    def __init__(self, start_date: date = date.today(), length: int = 0):
        """
        Заголовок с датами

        :param start_date: начальная дата отображения
        :param length: количество дней для отображения
        """
        self.start_date = start_date
        self.length = length

        self.cell_width = 4

        self.left_border = False
        self.right_border = False
        self.month_inner_borders = False
        self.inner_borders = False

        self.month_inner_border_char = Border(t=True, b=True)
        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)

    def render_months(self) -> str:
        mr = MonthRow(self.start_date, self.length)
        mr.cell_width = self.cell_width

        # Устанавливаем левую границу
        mr.left_border = self.left_border
        mr.left_border_char = self.left_border_char

        # Устанавливаем правую границу
        mr.right_border = self.right_border
        mr.right_border_char = self.right_border_char

        # Устанавливаем границы между ячейками
        mr.inner_borders = self.inner_borders

        # Устанавливаем границы между месяцами
        mr.month_inner_border = self.month_inner_borders
        mr.month_inner_border_char = self.month_inner_border_char

        return mr.render()

    def render_days(self) -> str:
        dr = DaysRow(self.start_date, self.length)
        dr.cell_width = self.cell_width

        # Устанавливаем левую границу
        dr.left_border = self.left_border
        dr.left_border_char = self.left_border_char

        # Устанавливаем правую границу
        dr.right_border = self.right_border
        dr.right_border_char = self.right_border_char

        # Устанавливаем границы между ячейками
        dr.inner_borders = self.inner_borders
        dr.inner_border_char = self.inner_border_char

        # Устанавливаем границы между месяцами
        dr.month_inner_borders = self.month_inner_borders
        dr.month_inner_border_char = self.month_inner_border_char

        return dr.render()

    def render_weekdays(self) -> str:
        wr = WeekdaysRow(self.start_date, self.length)
        wr.cell_width = self.cell_width

        # Устанавливаем левую границу
        wr.left_border = self.left_border
        wr.left_border_char = self.left_border_char

        # Устанавливаем правую границу
        wr.right_border = self.right_border
        wr.right_border_char = self.right_border_char

        # Устанавливаем границы между ячейками
        wr.inner_borders = self.inner_borders
        wr.inner_border_char = self.inner_border_char

        # Устанавливаем границы между месяцами
        wr.month_inner_borders = self.month_inner_borders
        wr.month_inner_border_char = self.month_inner_border_char

        return wr.render()

    def render(self) -> str:
        """
        Рендер заголовка с датами.
        Возвращает строковое представление этого заголовка.

        :return:
        """
        s = '\n'.join([self.render_months(), self.render_days(), self.render_weekdays()])
        return s
