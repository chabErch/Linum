from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.day import Day


class TestDay(TestCase):

    def test_pre_render(self):
        # Пререндер пустой ячейки
        d = Day()
        self.assertEqual('', d.pre_render())

        # Пререндер обычной ячейки
        d = Day(date_=date(2020, 1, 1))
        d.cell_width = 3
        self.assertEqual('1', d.pre_render())
