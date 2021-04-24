from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.month_cell import MonthCell


class TestMonthCell(TestCase):

    def test_pre_render(self):
        # Обычный пререндер
        mc = MonthCell(content=date(2020, 1, 1))
        self.assertEqual('January `20', mc.pre_render())
