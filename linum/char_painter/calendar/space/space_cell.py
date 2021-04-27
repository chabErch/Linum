from datetime import date
from typing import Optional, Any

from linum.char_painter.base import DateCell


class SpaceCell(DateCell):

    def __init__(self, cell_width: int = 0, date_: Optional[date] = None):
        super().__init__(cell_width, date_)

    @property
    def content(self):
        return ''

    @content.setter
    def content(self, any_: Any):
        """
        Заглушка. Не вносит никаких изменений.
        Необходима для корректного вызова конструктора родительского класса.

        :param any_: Any
        """
        pass
