from datetime import date
from unittest import TestCase

from linum.layer import Layer
from linum.layer_list import LayerList
from linum.task import Task
from linum.task_part import TaskPart


class TestLayerList(TestCase):

    def setUp(self) -> None:
        t = Task('', date(2020, 1, 2), 2)
        tp = TaskPart(t)
        self.l = Layer([tp])
        self.ll = LayerList([self.l])
        self.empty_ll = LayerList()

    def test_split(self):
        # Разделение пустого списка слоев
        self.assertEqual((self.empty_ll, self.empty_ll), self.empty_ll.split(date(2020, 1, 1)))

        # Разделение списка слева
        ll = LayerList([Layer()])
        self.assertEqual((ll, self.ll), self.ll.split(date(2020, 1, 1)))

        # Разделение списка справа
        self.assertEqual((self.ll, ll), self.ll.split(date(2020, 1, 10)))

        # Разделение списка с одним слоем, содержащим одну задачу
        left_l, right_l = self.l.split(date(2020, 1, 3))
        self.assertEqual((LayerList([left_l]), LayerList([right_l])), self.ll.split(date(2020, 1, 3)))
