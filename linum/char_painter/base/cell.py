from typing import Any

from linum.char_painter.base.border import Border
from linum.char_painter.enums import Align


class Cell:

    def __init__(self, cell_width: int = 0, content: Any = ''):
        """
        Ячейка.

        :param cell_width: ширина ячейки в символах;
        :param content: текстовое содержимое.
        """
        self.cell_width = cell_width
        self.content = content

        self.left_border = False
        self.right_border = False
        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.fill_char = Border()
        self.align: Align = Align.CENTER

    def __repr__(self):
        return "<Cell: '{}'>".format(self.content)

    def __len__(self):
        return len(self.render())

    def __bool__(self):
        if self.cell_width <= 0:
            return False
        return bool(self.content)

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        for k, v in self.__dict__.items():
            if getattr(other, k) != v:
                return False
        return True

    def draw_over(self, content: str) -> None:
        """
        Устанавливает содержимое ячейки поверх предыдущего значения.

        :param content: новое содержимое;
        """
        chars = list(self.content)
        self.content = ''.join([content] + chars[len(content):])

    def pre_render(self) -> str:
        """
        Предварительный рендер содержимого ячейки.
        Возвращает строковое представление содержимого без границ.

        :return: str
        """
        return str(self.content)

    def render(self) -> str:
        """
        Возвращает ASCII представление ячейки.

        :return: str
        """
        s = self.pre_render()

        # Обрезаем содержимое, если не влезает в ячейку.
        cell_width = max(0, self.cell_width)
        if len(s) > cell_width:
            s = s[:cell_width - 1] + "…"
        if cell_width == 0:
            s = ''

        # Выравниваем содержимое.
        if self.align is Align.LEFT:
            while len(s) < cell_width:
                s += str(self.fill_char)
        elif self.align is Align.RIGHT:
            while len(s) < cell_width:
                s = str(self.fill_char) + s
        elif self.align is Align.CENTER:
            position = int(cell_width / 2 - len(s) / 2)
            prefix = str(self.fill_char) * position
            postfix = str(self.fill_char) * (cell_width - len(prefix) - len(s))
            s = prefix + s + postfix

        # Рисуем границы ячейки.
        if self.left_border:
            s = str(self.left_border_char) + s
        if self.right_border:
            s += str(self.right_border_char)
        return s
