from datetime import date, timedelta
from typing import List, Any

from linum.char_painter.base.border import Border
from linum.char_painter.base.row import Row
from linum.char_painter.calendar.header.day import Day


class DaysRow(Row):

    def __init__(self, start_date: date, length: int):
        """
        Строка с датами.

        :param start_date: начальная дата для отображения
        :param length: количество отображаемых дней
        """
        self.length = length
        self.start_date = start_date

        self.cell_width = 4
        self.month_inner_borders = False
        self.month_inner_border_char = Border(t=True, b=True)
        super().__init__(self.cells)

    def __repr__(self):
        return "<DaysRow: '{}'>".format(self.start_date.strftime('%B'))

    @property
    def cells(self) -> List[Day]:
        """
        Возвращает список с ячейками-датами.

        :return: List[Day]
        """
        dates = [self.start_date + timedelta(i) for i in range(self.length)]
        cells = [Day(self.cell_width, d) for d in dates]
        return cells

    @cells.setter
    def cells(self, any_: Any):
        """
        Заглушка. Не вносит никаких изменений.
        Необходима для корректного вызова конструктора родительского класса.

        :param any_:
        """
        pass

    def pre_render(self) -> List[str]:
        """
        Пререндер списка с датами.
        Возвращает список отрендеренных ячеек.

        :return: List[str]
        """
        if len(self.cells) == 0:
            return []

        cells = []
        for cell in self.cells:
            # Добавляем границу между месяцами
            if cell.date.day == 1:
                cell.left_border = self.month_inner_borders and not self.inner_borders
                cell.left_border_char = self.month_inner_border_char
            cells.append(cell)
        cells[0].left_border = False

        # рендерим ячейки
        s = [c.render() for c in cells]
        return s
