from datetime import date
from typing import Optional

from linum.svg_renderer.base.style import Style
from linum.svg_renderer.calendar.header.weekday.weekday_cell import WeekdayCell


class DayOffWeekdayCell(WeekdayCell):

    def __init__(self, date_: date, width: float,
                 style: Optional[Style] = None):
        super().__init__(date_, width, style)

    @classmethod
    def get_class(cls):
        return "day-off"
