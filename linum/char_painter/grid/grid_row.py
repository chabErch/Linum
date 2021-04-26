from typing import Optional, List, Union

from linum.char_painter.base.border import Border
from linum.char_painter.grid.grid_cell import GridCell


class GridRow:

    def __init__(self, cells: Optional[List[GridCell]] = None):
        """
        Строка сетки.

        :param cells: ячейки сетки
        """
        self.cells = cells or []

        self.left_border = False
        self.right_border = False
        self.inner_borders = False
        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)

    def __or__(self, other):
        if not isinstance(other, GridRow):
            raise TypeError

        # Разная размерность
        if len(self.cells) != len(other.cells):
            raise TypeError("Cells count must be equal for |: {} != {}".format(len(self.cells), len(other.cells)))

        # складываем ячейки
        gr = GridRow()
        for i in range(len(self.cells)):
            gc = self.cells[i] | other.cells[i]
            gr.append(gc)

        # Складываем левую границу
        gr.left_border = self.left_border or other.left_border
        gr.left_border_char = self.left_border_char + other.left_border_char

        # Складываем правую границу
        gr.right_border = self.right_border or other.right_border
        gr.right_border_char = self.right_border_char or other.right_border_char

        # Складываем внутреннюю границу
        gr.inner_borders = self.inner_borders or other.inner_borders
        gr.inner_border_char = self.inner_border_char or other.inner_border_char

        return gr

    def append(self, cells: Union[List[GridCell], GridCell]):
        """
        Добавление в конец строки указанных ячеек.

        :param cells: ячейки для добавления
        """
        if isinstance(cells, list):
            self.cells += cells
        elif isinstance(cells, GridCell):
            self.cells.append(cells)

    def prerender(self) -> List[Border]:
        """
        Пререндер строки. Возвращает список из одних границ.

        :return: List[Border]
        """
        if not self.cells:
            return []
        # Сливаем все ячейки и их границы в массив границ
        borders = self.cells[0].pre_render()
        for i in range(len(self.cells) - 1):
            if self.inner_borders:
                # Сливаем соседние границы ячеек в одну границу
                lb = self.cells[i].right_border_char if self.cells[i].right_border else Border()
                rb = self.cells[i + 1].left_border_char if self.cells[i + 1].left_border else Border()
                borders.append(lb + rb + self.inner_border_char)
            borders += self.cells[i + 1].pre_render()
        return borders

    def render(self) -> str:
        """
        Рендер строки. Возвращает строковое представление строки.

        :return: str
        """
        borders = self.prerender()

        # Ставим левую границу
        if self.left_border:
            borders = [self.left_border_char] + borders

        # Ставим правую границу
        if self.right_border:
            borders += [self.right_border_char]

        borders_str = [str(b) for b in borders]
        s = ''.join(borders_str)
        return s

    def merge(self) -> GridCell:
        """
        Сливает ячейки строки в одну ячейку.

        :return:
        """
        borders = self.prerender()
        gc = GridCell(cell_width=len(borders), content=borders)
        gc.left_border = self.left_border
        gc.left_border_char = self.left_border_char
        gc.right_border = self.right_border
        gc.right_border_char = self.right_border_char
        return gc
