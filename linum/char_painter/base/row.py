from typing import List, Union, Optional

from linum.char_painter.base.border import Border
from linum.char_painter.base.cell import Cell
from linum.char_painter.enums import Align


class Row:

    def __init__(self, cells: Optional[List[Cell]] = None):
        """
        Строка, которая умеет в ASCII.

        :param cells: список ячеек для отображения.
        """
        self.cells = cells or []

        self.left_border = False
        self.right_border = False
        self.inner_borders = False
        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)
        self.align: Align = Align.CENTER

    def __repr__(self):
        return "<Row: with {} cells>".format(len(self.cells))

    def __len__(self):
        return len(self.render())

    def __getitem__(self, item):
        return self.cells[item]

    def __add__(self, other):
        if isinstance(other, Row):
            self.cells += other.cells
            return self
        elif isinstance(other, Cell):
            self.cells += [other]
            return self
        raise TypeError("unsupported operand type for +: 'Row' and '{}'".format(type(other)))

    def __bool__(self):
        if not self.cells:
            return False
        for cell in self.cells:
            if cell:
                return True
        return False

    def append(self, cells: Union[List[Cell], Cell]):
        """
        Добавляет в конец указанные ячейки.

        :param cells: ячейка или список ячеек для добавления
        """
        if isinstance(cells, list):
            self.cells += cells
        elif isinstance(cells, Cell):
            self.cells.append(cells)

    def pre_render(self) -> List[str]:
        """
        Предварительный рендер содержимого строки.
        Возвращает список отрендеренных ячеек.

        :return: List[str]
        """
        cells_str = []
        for c in self.cells:
            cells_str += [c.render()]
        return cells_str

    def render(self) -> str:
        """
        Возвращает символьное представление строки.

        :return: str
        """
        # Рендерим ячеки
        cells_str = self.pre_render()

        # Рисуем внутренние границы
        ch = str(self.inner_border_char) if self.inner_borders else ''
        s = ch.join(cells_str)

        # Рисуем левую границу
        if self.left_border:
            s = str(self.left_border_char) + s

        # Рисуем правую границу
        if self.right_border:
            s += str(self.right_border_char)

        return s

    def merge(self, content='', align: Align = Align.CENTER) -> Cell:
        """
        Объединяет все ячейки строки в одну.

        :param content: содержимое для созданной ячейки
        :param align:
        :return: Cell
        """
        width = len(self)
        if self.left_border:
            width -= 1
        if self.right_border:
            width -= 1
        cell = Cell(width)  # todo 2: Добавить слияние содержимого
        cell.content = content
        cell.align = align
        cell.left_border = self.left_border
        cell.right_border = self.right_border
        cell.left_border_char = self.left_border_char
        cell.right_border_char = self.right_border_char
        return cell
