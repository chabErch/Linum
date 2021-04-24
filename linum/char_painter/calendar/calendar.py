from datetime import date, timedelta
from typing import List, Tuple

from linum.char_painter.calendar.header.header import Header
from linum.char_painter.calendar.layer_list_view import LayerListView
from linum.context import Context
from linum.helper import days_in_month
from linum.layer_list import LayerList


class Calendar:

    def __init__(self, layer_list: LayerList, context: Context):
        """
        Календарь с задачами.

        :param layer_list: список слоев с кусочками задач
        :param context: контекст отображения
        """
        self.context = context
        self.layer_list = layer_list

    def render_row(self, start_date: date, length: int) -> str:
        """
        Рендер одной строки календаря.
        В рендер включаются заголовок с названием месяца, датами и днями недели,
        а также строковое представление слоев в уазанный диапазон отображения.

        :param start_date: начальная дата отображения
        :param length: продолжительность периода отображения
        :return: str
        """
        # Формируем заголовок
        h = Header(start_date, length)
        h.cell_width = self.context.cell_width
        h.inner_borders = self.context.inner_borders
        h.month_inner_borders = self.context.month_inner_borders
        h.left_border = self.context.left_border
        h.right_border = self.context.right_border

        # Формируем представление слоев
        llv = LayerListView(self.layer_list, start_date, length)
        llv.cell_width = self.context.cell_width
        llv.inner_borders = self.context.inner_borders
        llv.left_border = self.context.left_border
        llv.right_border = self.context.right_border

        s = '\n'.join([h.render(), llv.render()])
        return s

    def render(self) -> str:
        """
        Рендер полного календаря.
        Возвращает строковое представление календаря с задачами.

        :return:
        """
        rendered_rows = []
        for date_, length in self._get_date_limits():
            rendered_rows.append(self.render_row(date_, length))

        s = '\n\n'.join(rendered_rows)
        return s

    def _get_date_limits(self) -> List[Tuple[date, int]]:
        """
        Формирует список - по одному элементу на месяц.
        Каждый элемент списка - кортеж из отображаемой начальной даты месяца
        и продолжительности месяца в днях.

        :return: List[Tuple[date, int]]
        """
        # Если период отображения начинается не с первого числа,
        # то добавляем заданную начальную дату
        months_first_dates = []
        if self.context.start_date.day != 1:
            months_first_dates.append(self.context.start_date)

        # Запоминаем каждое первое число каждого месяца
        for i in range(self.context.length):
            if (self.context.start_date + timedelta(i)).day == 1:
                months_first_dates.append(self.context.start_date + timedelta(i))

        result = []
        for i in range(0, len(months_first_dates), self.context.months_in_row):
            months_first_dates_in_row = months_first_dates[i: i + self.context.months_in_row]
            length = 0
            for d in months_first_dates_in_row:
                length += days_in_month(d) if d.day == 1 else days_in_month(d) - d.day

            result.append((months_first_dates_in_row[0], length))

        return result
