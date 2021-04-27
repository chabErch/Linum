from datetime import date
from unittest import TestCase

from linum.helper import split_by_months


class Test(TestCase):

    def test_split_by_months(self):
        # Разделение первого дня месяца
        self.assertEqual([(date(2020, 1, 1), 1)], split_by_months(date(2020, 1, 1), 1))

        # Разделение не первого дня месяца
        self.assertEqual([(date(2020, 1, 2), 1)], split_by_months(date(2020, 1, 2), 1))

        # Разделение двух дней перед границей месяца
        self.assertEqual([(date(2020, 1, 30), 2)], split_by_months(date(2020, 1, 30), 2))

        # Разделение двух дней на границе месяца
        self.assertEqual([(date(2020, 1, 31), 1), (date(2020, 2, 1), 1)], split_by_months(date(2020, 1, 31), 2))

        # Разделение двух дней после границы месяца
        self.assertEqual([(date(2020, 1, 1), 2)], split_by_months(date(2020, 1, 1), 2))

        # Разделение, включающее полный месяц
        result = [(date(2020, 1, 30), 2), (date(2020, 2, 1), 29), (date(2020, 3, 1), 1)]
        self.assertEqual(result, split_by_months(date(2020, 1, 30), 32))
