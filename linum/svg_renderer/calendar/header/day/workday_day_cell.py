from datetime import date
from typing import Optional, List

from linum.svg_renderer.base.style import Style
from linum.svg_renderer.calendar.header.day.day_cell import DayCell


class WorkdayDayCell(DayCell):

    def __init__(self, date_: date, width: float, style: Optional[Style] = None):
        super().__init__(date_, width, style)

    @classmethod
    def get_class(cls):
        return "workday"
