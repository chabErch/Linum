from copy import copy
from typing import List, Optional

from linum.char_painter.base.border import Border


class GridCell:

    def __init__(self, cell_width: int = 0, content: Optional[List[Border]] = None):
        """
        Сеточная ячейка. Нужна для рисования сеток.

        :param cell_width: ширина ячейки в символах
        :param content: содержимле ячейки
        """
        self.cell_width = cell_width
        self.content = content or []

        self.left_border = False
        self.right_border = False

        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)

        self.fill_char = Border()

    def __eq__(self, other):
        if not isinstance(other, GridCell):
            return False
        for k, v in self.__dict__:
            if not getattr(other, k) == v:
                return False
        return True

    def __or__(self, other):
        if not isinstance(other, GridCell):
            raise TypeError

        if self.cell_width != other.cell_width:
            raise TypeError("Border lengths must be equal for |: {} != {}".format(self.cell_width, other.cell_width))

        gc = GridCell()
        self_borders = self.pre_render()
        other_borders = other.pre_render()
        for i in range(self.cell_width):
            b = self_borders[i] + other_borders[i]
            gc.content.append(b)

        # Устанавливаем левую границу
        gc.left_border = self.left_border or other.left_border
        gc.left_border_char = self.left_border_char + other.left_border_char

        # Устанавливаем правую границу
        gc.right_border = self.right_border or other.right_border
        gc.right_border_char = self.right_border_char or other.right_border_char

        return gc

    def pre_render(self) -> List[Border]:
        """
        Предварительный рендер ячейки.
        Возвращает список границ без правой и левой границ.

        :return:
        """
        if self.cell_width == 0:
            return []

        # Дополняем ячейки до заданной длины
        borders = self.content
        while len(borders) < self.cell_width:
            borders.append(copy(self.fill_char))

        # Обрезаем лишние ячейки, если они есть
        borders = borders[:self.cell_width]

        return borders

    def render(self):
        """
        Рендер содержимого ячейки.
        Возвращает строковое представление ячейки.

        :return:
        """
        borders = self.pre_render()

        # Рендеримм содержимое ячейки
        borders_str = [str(borders[i]) for i in range(self.cell_width)]
        s = ''.join(borders_str)

        # Рендерим левую границу
        if self.left_border:
            s = str(self.left_border_char) + s

        # Рендерим правую границу
        if self.right_border:
            s += str(self.right_border_char)

        return s
