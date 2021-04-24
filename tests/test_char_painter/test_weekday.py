from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.weekday import Weekday


class TestWeekday(TestCase):

    def test_pre_render(self):
        # Обычный пререндер
        w = Weekday(date_=date(2020, 1, 1))
        self.assertEqual('Wed', w.pre_render())
