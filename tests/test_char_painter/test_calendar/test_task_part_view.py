from datetime import date
from unittest import TestCase

from linum import Task
from linum.char_painter.base.cell import Cell
from linum.char_painter.calendar.task_part_view import TaskPartView
from linum.char_painter.enums import Align
from linum.task_part import TaskPart


class TestTaskPartView(TestCase):

    def setUp(self) -> None:
        t = Task('Task 1', date(2020, 1, 30), 4)
        tp_1 = TaskPart(t, length=2)
        tp_2 = TaskPart(t, start_date=date(2020, 2, 1))
        tp_3 = TaskPart(t)
        self.cell_width = 3
        self.tpv_1 = TaskPartView(tp_1)
        self.tpv_1.cell_width = self.cell_width
        self.tpv_2 = TaskPartView(tp_2)
        self.tpv_2.cell_width = self.cell_width
        self.tpv_3 = TaskPartView(tp_3)
        self.tpv_3.cell_width = self.cell_width

    def test_get_middle_segment(self):
        # Отображение задачи длиной в два дня перед концом месяца
        c = Cell(cell_width=6, content='│Tas…│')
        self.assertEqual(c, self.tpv_1.pre_render_middle_segment())

        # Отображение задачи с внутренними  границами
        self.tpv_1.inner_borders = True
        c = Cell(cell_width=7, content='Task 1')
        c.left_border = True
        c.right_border = True
        c.align = Align.LEFT
        self.assertEqual(c, self.tpv_1.pre_render_middle_segment())

        # Отображение задачи длиной в два дня в начале месяца
        c = Cell(cell_width=6, content='│Tas…│')
        self.assertEqual(c, self.tpv_2.pre_render_middle_segment())

        # Отображение задачи на границе месяца
        c = Cell(cell_width=12, content='│Task 1    │')
        self.assertEqual(c, self.tpv_3.pre_render_middle_segment())

        # Отображение задачи на границе месяца с разделением по месяцам
        c = Cell(cell_width=13, content='│Task 1     │')
        self.tpv_3.month_inner_borders = True
        self.assertEqual(c, self.tpv_3.pre_render_middle_segment())

        # Отображение задачи на границе месяца с внутренним разделением
        c = Cell(cell_width=15, content='Task 1')
        c.left_border = True
        c.right_border = True
        c.align = Align.LEFT
        self.tpv_3.month_inner_borders = False
        self.tpv_3.inner_borders = True
        self.assertEqual(c, self.tpv_3.pre_render_middle_segment())
