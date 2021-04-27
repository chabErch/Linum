from datetime import date
from unittest import TestCase

from linum.char_painter.calendar.header.weekday import Weekday


class TestWeekday(TestCase):

    def test_pre_render(self):
        # Пререндер пустой ячейки
        d = Weekday()
        self.assertEqual('', d.pre_render())

        # Пререндер ячейки с отрицательной длиной
        d = Weekday()
        d.cell_width = -10
        self.assertEqual('', d.pre_render())

        # Пререндер обычной ячейки
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 3
        self.assertEqual('Wed', d.pre_render())

    def test_render(self):
        # Рендер пустой ячейки
        d = Weekday()
        self.assertEqual('', d.render())

        # Рендер ячейки с отрицательной длиной
        d = Weekday()
        d.cell_width = -10
        self.assertEqual('', d.render())

        # Рендер обычной ячейки
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 3
        self.assertEqual('Wed', d.render())

        # Рендер ячейки с левой границей
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 3
        d.left_border = True
        self.assertEqual('│Wed', d.render())

        # Рендер ячейки с правой границей
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 3
        d.right_border = True
        self.assertEqual('Wed│', d.render())

        # Рендер ячейки с двумя границами
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 3
        d.left_border = True
        d.right_border = True
        self.assertEqual('│Wed│', d.render())

        # Рендер ячейки нулевой длины с двумя границами
        d = Weekday(date_=date(2020, 1, 1))
        d.cell_width = 0
        d.left_border = True
        d.right_border = True
        self.assertEqual('││', d.render())
