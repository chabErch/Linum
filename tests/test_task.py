from datetime import date
from unittest import TestCase

from linum.task import Task


class TestTask(TestCase):

    def test_day_after(self):
        # Обычная задача
        t = Task(start_date=date(2020, 1, 1), length=2)
        self.assertEqual(date(2020, 1, 3), t.day_after)

        # Задача нулевой длины
        t = Task(start_date=date(2020, 1, 1), length=0)
        self.assertEqual(date(2020, 1, 1), t.day_after)

        # Задача отрицательой длины
        t = Task(start_date=date(2020, 1, 1), length=-10)
        self.assertEqual(date(2020, 1, 1), t.day_after)
