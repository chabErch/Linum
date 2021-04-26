from datetime import timedelta, date
from typing import List, Tuple

from linum.char_painter.enums import Align


def days_in_month(date_: date.today()) -> int:
    """
    Возвращает количество дней в месяце для указанной даты.

    :param date_: дата, месяц которой необходимо вычислить
    :return: int
    """
    year = date_.year
    month = date_.month
    next_month = month + 1 if month + 1 < 13 else 1
    d = date(year=year, month=next_month, day=1)
    last_day_in_month = d - timedelta(days=1)
    return last_day_in_month.day


def split_by_months(start_date: date, length: int) -> List[Tuple[date, int]]:
    """
    Разделяет указанный период по месяцам.
    Возвращает список с кортежами - по одному на месяц.
    Каждый кортеж представляет из себя начальную дату месяца
    и количество дней в месяце.
    Если заданный период начинается не с начала месяца,
    то соответствующий кортеж будет указывать на заданную начальную дату
    и количество дней до конца месяца.

    :param start_date: начальная дата анализируемого периода
    :param length: продолжительность периода
    :rtype: List[Tuple[date, int]]
    """
    if length <= 0:
        return [(start_date, 0)]

    # Получаем список всех дат периода
    dates = [start_date + timedelta(i) for i in range(length)]

    months = []
    previous = 0
    # Разделяем список дат на месяцы
    for i in range(len(dates)):
        if dates[i].day == 1:
            months.append(dates[previous: i])
            previous = i
    # Добавляем последний промежуток
    months.append(dates[previous:])

    # Корректируем список
    if start_date.day == 1:
        months.pop(0)

    result = []
    # Формируем результат
    for month in months:
        result.append((month[0], len(month)))

    return result


def supp_content(content: str, length: int, align: Align = Align.LEFT, fill_char: str = ' ') -> str:
    """
    Дополнгяет строку до указанной длины символами `fill_char`.

    :param content: содержимое для выравнивания
    :param length: требуемая длина
    :param align: выравнивание
    :param fill_char: символ заполнения
    :return: str
    """
    if len(content) >= length:
        return content

    # Дополняем символами справа
    if align is Align.LEFT:
        while len(content) < length:
            content += str(fill_char)

    # Дополняем символами слева
    elif align is Align.RIGHT:
        while len(content) < length:
            content = str(fill_char) + content

    # Дополняем символами с обеих сторон
    elif align is Align.CENTER:
        position = int(length / 2 - len(content) / 2)
        prefix = str(fill_char) * position
        postfix = str(fill_char) * (length - len(prefix) - len(content))
        content = prefix + content + postfix
    return content


def trim_content(content: str, length: int) -> str:
    """
    Оборезает содержимое до указанной длины.

    :param content: содержимое для обрезания
    :param length: требуемая длина
    :return: str
    """
    if length <= 0:
        return ''
    if len(content) > length:
        return content[:length - 1] + "…"
    return content
