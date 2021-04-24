from unittest import TestCase

from linum.char_painter.base.border import Border
from linum.char_painter.grid.grid_cell import GridCell


class TestGridCell(TestCase):

    def test_prerender(self):
        # Пререндер пустой ячейки
        gc = GridCell()
        self.assertEqual([], gc.prerender())

        # Пререндер обычной ячейки
        gc = GridCell(cell_width=1)
        self.assertEqual([Border()], gc.prerender())

        # Преендер обычной ячейки двойной ширины
        gc = GridCell(cell_width=2)
        self.assertEqual([Border()] * 2, gc.prerender())

        # Пререндер предопределенной ячейки
        b = Border(l=True, b=True)
        gc = GridCell(cell_width=1, content=[b])
        self.assertEqual([b], gc.prerender())

        # Пререндер ячейки с границами
        gc.left_border = True
        gc.right_border = True
        self.assertEqual([b], gc.prerender())

    def test_render(self):
        # Рендер пустой ячейки
        gc = GridCell()
        self.assertEqual('', gc.render())

        # Рендер пустой ячейки
        gc = GridCell(cell_width=1)
        self.assertEqual(' ', gc.render())

        # Рендер пустой ячейки двойной ширины
        gc = GridCell(cell_width=2)
        self.assertEqual('  ', gc.render())

        # Рендер предопределенной ячейки
        b = Border(r=True, b=True)
        gc = GridCell(cell_width=2, content=[b])
        self.assertEqual('┌ ', gc.render())

        # Рендер ячейки с границами
        gc.left_border = True
        gc.right_border = True
        self.assertEqual('│┌ │', gc.render())

        pass
