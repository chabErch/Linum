from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.weekdays_row import WeekdaysRow


class TestWeekdaysRow(TestCase):

    def test_pre_render(self):
        # Обычный пререндер
        wr = WeekdaysRow(start_date=date(2020, 1, 1), length=7)
        wr.cell_width = 3
        self.assertEqual(['Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue'], wr.pre_render())

        # Пререндер строки с пустыми ячейками
        wr = WeekdaysRow(start_date=date(2020, 1, 1), length=7)
        wr.cell_width = 0
        self.assertEqual(['', '', '', '', '', '', ''], wr.pre_render())
