from datetime import date, timedelta
from typing import List, Any

from linum.char_painter.calendar.header.days_row import DaysRow
from linum.char_painter.calendar.header.weekday import Weekday


class WeekdaysRow(DaysRow):

    def __init__(self, start_date: date = date.today(), length: int = 0):
        """
        Строка с днями недели.

        :param start_date: начальная дата для отображения в качестве дня недели
        :param length: количество отображаемых дней
        """
        super().__init__(start_date=start_date, length=length)

    def __repr__(self):
        return "<WeekdaysRow: '{}'>".format(self.start_date.strftime('%B'))

    @property
    def cells(self) -> List[Weekday]:
        """
        Возвращает список с ячейками - днями недели.

        :return: List[Weekday]
        """
        dates = [self.start_date + timedelta(i) for i in range(self.length)]
        cells = [Weekday(self.cell_width, d) for d in dates]
        return cells

    @cells.setter
    def cells(self, any_: Any):
        """
        Заглушка. Не вносит никаких изменений.
        Необходима для корректного вызова конструктора родительского класса.

        :param any_:
        """
        pass
