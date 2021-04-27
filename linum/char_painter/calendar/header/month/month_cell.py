from datetime import date
from typing import Any

from linum.char_painter.base import DateCell


class MonthCell(DateCell):

    def __init__(self, cell_width: int = 0, date_: date = date.today()):
        """
        Ячейка с названием месяца.

        :param cell_width: ширина ячейки в символах;
        :param date_: дата, месяц которой необходимо отобразить.
        """
        super().__init__(cell_width, date_)

    def __repr__(self):
        return "<MonthCell at {} with width {}>".format(self.content, self.cell_width)

    @property
    def content(self) -> str:
        """
        Возвращает строку с названием дня недели.

        :return: str
        """
        if isinstance(self.date, date):
            return self.date.strftime('%B') + ' `' + self.date.strftime('%y')
        return ''

    @content.setter
    def content(self, any_: Any):
        """
        Заглушка. Не вносит никаких изменений.
        Необходима для корректного вызова конструктора родительского класса.

        :param any_: Any
        """
        pass

    # def pre_render(self) -> str:
    #     """
    #     Пререндер ячейки с названием месяца.
    #     Возвращает строковое представление ячейки без внешних границ.
    #
    #     :return:
    #     """
    #     return self.content.strftime('%B') + ' `' + self.content.strftime('%y')