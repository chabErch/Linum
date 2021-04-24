from datetime import date
from unittest import TestCase

from linum.task import Task
from linum.task_part import TaskPart


class TestTaskPart(TestCase):

    def setUp(self) -> None:
        self.task = Task('1234', start_date=date(2020, 1, 3), length=2)

    def test_start_date(self):
        # Часть, соответствующая задаче
        tp = TaskPart(self.task)
        self.assertEqual(date(2020, 1, 3), tp.start_date)

        # Часть, начинающаяся до задачи
        tp = TaskPart(self.task, start_date=date(2020, 1, 1))
        self.assertEqual(date(2020, 1, 3), tp.start_date)

        # Часть, с продолжительностью, большей чем продолжительность задачи
        tp = TaskPart(self.task, length=4)
        self.assertEqual(date(2020, 1, 3), tp.start_date)

        # Часть, с начальной датой, большей начальной даты задачи
        tp = TaskPart(self.task, length=4)
        self.assertEqual(date(2020, 1, 3), tp.start_date)

    def test_day_after(self):
        # Часть, соответствующая задаче
        tp = TaskPart(self.task)
        self.assertEqual(date(2020, 1, 5), tp.day_after)

        # Часть с нулевой длиной
        tp = TaskPart(self.task, length=0)
        self.assertEqual(date(2020, 1, 3), tp.day_after)

        # Часть с ненулевой длиной
        tp = TaskPart(self.task, length=1)
        self.assertEqual(date(2020, 1, 4), tp.day_after)

        # Часть, начинающаяся до задачи
        tp = TaskPart(self.task, start_date=date(2020, 1, 1))
        self.assertEqual(date(2020, 1, 5), tp.day_after)

        # Часть, с продолжительностью, большей чем продолжительность задачи
        tp = TaskPart(self.task, length=4)
        self.assertEqual(date(2020, 1, 5), tp.day_after)

        # Часть, с начальной датой, большей начальной даты задачи
        tp = TaskPart(self.task, length=4)
        self.assertEqual(date(2020, 1, 3), tp.start_date)

    def test_split(self):
        # Разделение пустой ячейки
        tp = TaskPart(self.task, length=0)
        ltp = TaskPart(self.task, length=0)
        self.assertEqual((ltp, None), tp.split(date(2020, 1, 3)))

        # Разделение обычной ячейки
        tp = TaskPart(self.task)
        ltp = TaskPart(self.task, length=1)
        rtp = TaskPart(self.task, start_date=date(2020, 1, 4), length=1)
        rtp.is_tail = True
        self.assertEqual((ltp, rtp), tp.split(date(2020, 1, 4)))

        # Еще одно разделение обычной ячейки
        t = Task('', date(2020, 1, 1), 2)
        tp = TaskPart(t)
        ltp = TaskPart(t, length=1)
        rtp = TaskPart(t, start_date=date(2020, 1, 2), length=1)
        rtp.is_tail = True
        self.assertEqual((ltp, rtp), tp.split(date(2020, 1, 2)))

        # Разделение слева
        tp = TaskPart(self.task)
        self.assertEqual((None, tp), tp.split(date(2020, 1, 1)))

        # Разделение справа
        tp = TaskPart(self.task)
        self.assertEqual((tp, None), tp.split(date(2020, 1, 10)))
