from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.day import Day


class TestDay(TestCase):

    def test_pre_render(self):
        # Обычный пререндер
        d = Day(date_=date(2020, 1, 1))
        self.assertEqual('1', d.pre_render())
