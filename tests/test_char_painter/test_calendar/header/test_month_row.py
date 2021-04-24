from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.month_cell import MonthCell
from linum.char_painter.calendar.header.month_row import MonthRow


class TestMonthRow(TestCase):

    def test_render(self):
        mr = MonthRow(date(2020, 1, 31), 1)
        self.assertEqual('Jan…', mr.render())

        mr = MonthRow(date(2020, 1, 31), 2)
        self.assertEqual('Jan…Feb…', mr.render())

        mr = MonthRow(date(2020, 1, 30), 4)
        self.assertEqual('January…Februar…', mr.render())

    def test_pre_render(self):
        # Пререндер строки с длиной 1
        mr = MonthRow(date(2020, 1, 31), 1)
        mc = MonthCell(cell_width=mr.cell_width, content=date(2020, 1, 31))
        self.assertEqual([mc], mr.pre_render())

        # Пререндер строки с датами на границе месяца
        mr = MonthRow(date(2020, 1, 31), 2)
        mc_1 = MonthCell(cell_width=mr.cell_width, content=date(2020, 1, 31))
        mc_2 = MonthCell(cell_width=mr.cell_width, content=date(2020, 2, 1))
        self.assertEqual([mc_1, mc_2], mr.pre_render())

        # Пререндер строки с расширенными датами на границе месяца
        mr = MonthRow(date(2020, 1, 30), 4)
        mc_1 = MonthCell(cell_width=mr.cell_width, content=date(2020, 1, 30))
        mc_2 = MonthCell(cell_width=mr.cell_width, content=date(2020, 2, 1))
        mc_1.cell_width = 8
        mc_2.cell_width = 8
        self.assertEqual([mc_1, mc_2], mr.pre_render())

        # Пререндер строки с полным месяцем
        mr = MonthRow(date(2020, 1, 1), 31)
        mc = MonthCell(cell_width=mr.cell_width, content=date(2020, 1, 1))
        mc.cell_width = 4 * 31
        self.assertEqual([mc], mr.pre_render())
