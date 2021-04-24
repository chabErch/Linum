from datetime import date, timedelta

from linum.char_painter.base.border import Border
from linum.char_painter.calendar.layer_view import LayerView
from linum.layer_list import LayerList


class LayerListView:

    def __init__(self, layer_list: LayerList, start_date: date = date.today(), length: int = 0):
        """
        Представление массива слоев.

        :param layer_list: массив слоев
        :param start_date: начальная дата отображения
        :param length: продолжительность
        """
        self.layer_list = layer_list
        self.length = length
        self.start_date = start_date

        self.cell_width = 4

        self.left_border = False
        self.right_border = False
        self.inner_borders = False

        self.left_border_char = Border(t=True, b=True)
        self.right_border_char = Border(t=True, b=True)
        self.inner_border_char = Border(t=True, b=True)

    def render(self) -> str:
        """
        Рендер массива слоев.
        Возвращает строковое представление этого массива.

        :return: str
        """
        # Обрезаем все, что выходит за границы
        layer_list = self._trim_layer_list()

        # Убираем пустые слои
        layer_list.cleanup()

        lines = []
        for layer in layer_list:
            # Формируем представление слоя
            lv = LayerView(layer, self.start_date, self.length)
            lv.cell_width = self.cell_width

            # Устанавливаем левую границу
            lv.left_border = self.left_border
            lv.left_border_char = self.left_border_char

            # Устанавливаем правую границу
            lv.right_border = self.right_border
            lv.right_border_char = self.right_border_char

            # Устанавливаем внутренние границы
            lv.inner_borders = self.inner_borders
            lv.inner_border_char = self.inner_border_char

            lines.append(lv.get_outline(is_top_outline=True))
            lines.append(lv.get_middle_segment())
            lines.append(lv.get_outline(is_top_outline=False))

        s = '\n'.join(lines)
        return s

    def _trim_layer_list(self) -> LayerList:
        _, layer_list = self.layer_list.split(self.start_date)
        layer_list, _ = layer_list.split(self.start_date + timedelta(self.length))
        return layer_list
