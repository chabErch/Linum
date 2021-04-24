from datetime import date
from unittest import TestCase

from linum.layer import Layer
from linum.task import Task
from linum.task_part import TaskPart


class TestLayer(TestCase):

    def setUp(self) -> None:
        t1 = Task('', start_date=date(2020, 1, 1), length=2)
        self.tp1 = TaskPart(t1)
        t2 = Task('', start_date=date(2020, 1, 4), length=2)
        self.tp2 = TaskPart(t2)
        t3 = Task('', start_date=date(2020, 1, 1), length=5)
        self.tp3 = TaskPart(t3)

    def test_split(self):
        # Разделение пустого слоя
        # self.assertEqual((Layer(), Layer()), Layer().split(date(2020, 1, 1)))

        # Разделение слоя с одной задачей
        l = Layer()
        l.append(self.tp1)
        ltp, rtp = self.tp1.split(date(2020, 1, 2))
        ll = Layer()
        ll.append(ltp)
        rl = Layer()
        rl.append(rtp)
        self.assertEqual((ll, rl), l.split(date(2020, 1, 2)))

        # Разделение слоя слева
        l = Layer()
        l.append(self.tp2)
        ll = Layer()
        self.assertEqual((ll, l), l.split(date(2020, 1, 1)))

        # Разделение слоя справа
        l = Layer()
        l.append(self.tp2)
        rl = Layer()
        self.assertEqual((l, rl), l.split(date(2020, 1, 10)))

