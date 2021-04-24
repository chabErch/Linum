from unittest import TestCase

from linum.char_painter.base.border import Border
from linum.char_painter.grid.grid_cell import GridCell
from linum.char_painter.grid.grid_row import GridRow


class TestGridRow(TestCase):

    def test_prerender(self):
        # Пререндер пустой строки
        gr = GridRow()
        self.assertEqual([], gr.prerender())

        # Пререндер строки из одной пустой ячейки
        gr = GridRow([GridCell()])
        self.assertEqual([], gr.prerender())

        # Пререндер строки из двух ячеек
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gr = GridRow([gc, gc])
        self.assertEqual([b, b], gr.prerender())

        # Пререндер строки из двух ячеек с внутренней границей
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gr = GridRow([gc, gc])
        gr.inner_borders = True
        self.assertEqual([b, gr.inner_border_char, b], gr.prerender())

        # Пререндер строки из двух ячеек с левыми границами без внутренних границ
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gc.left_border = True
        gr = GridRow([gc, gc])
        self.assertEqual([b, b], gr.prerender())

        # Пререндер строки из двух ячеек с левыми границами с внутренними границами
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gc.left_border = True
        gr = GridRow([gc, gc])
        gr.inner_borders = True
        self.assertEqual([b, gc.left_border_char, b], gr.prerender())

        # Пререндер строки из двух ячеек с правыми границами без внутренних границ
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gc.right_border = True
        gr = GridRow([gc, gc])
        self.assertEqual([b, b], gr.prerender())

        # Пререндер строки из двух ячеек с правыми границами с внутренними границами
        b = Border(l=True, b=True)
        gc = GridCell(1, [b])
        gc.right_border = True
        gr = GridRow([gc, gc])
        gr.inner_borders = True
        self.assertEqual([b, gc.right_border_char, b], gr.prerender())

        # Пререндер строки из двух ячеек с разными границами
        b = Border(l=True, r=True)
        gc = GridCell(1, [b])
        gc.right_border = True
        gc.right_border_char = b
        gr = GridRow([gc, gc])
        gr.inner_borders = True
        self.assertEqual([b, Border(l=True, r=True, t=True, b=True), b], gr.prerender())

    # def test_render(self):
    #     self.fail()
    #
    # def test_merge(self):
    #     self.fail()
