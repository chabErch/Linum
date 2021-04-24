from datetime import date

from linum.char_painter.base.cell import Cell


class MonthCell(Cell):

    def __init__(self, cell_width: int = 0, content: date = date.today()):
        """
        Ячейка с названием месяца.

        :param cell_width: ширина ячейки в символах;
        :param content: дата, месяц которой необходимо отобразить.
        """
        super().__init__(cell_width, content)

    def __repr__(self):
        return "<MonthCell at {} with width {}>".format(self.content, self.cell_width)

    def pre_render(self) -> str:
        """
        Пререндер ячейки с названием месяца.
        Возвращает строковое представление ячейки без внешних границ.

        :return:
        """
        return self.content.strftime('%B') + ' `' + self.content.strftime('%y')
