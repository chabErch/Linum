from datetime import date, timedelta
from typing import List, Optional

from linum.helper import is_day_off
from linum.svg_renderer.base.row import Row
from linum.svg_renderer.base.style import Style
from linum.svg_renderer.calendar.header.weekday.day_off_weekday_cell import DayOffWeekdayCell
from linum.svg_renderer.calendar.header.weekday.weekday_cell import WeekdayCell
from linum.svg_renderer.calendar.header.weekday.workday_weekday_cell import WorkdayWeekdayCell


class WeekdaysRow(Row):

    def __init__(self, start: date, length: int, width: float,
                 workday_style: Optional[Style] = None, day_off_style: Optional[Style] = None,
                 workdays: Optional[List[date]] = None, days_off: Optional[List[date]] = None):
        self.start = start
        self.length = length
        self.width = width

        self.workday_style = workday_style or Style()
        self.day_off_style = day_off_style or Style()

        self.workdays = workdays or []
        self.days_off = days_off or []

    @property
    def height(self) -> int:
        wd_height = self.workday_style.get("height", 100)
        do_height = self.day_off_style.get("height", 100)
        return max(wd_height, do_height)

    @property
    def cells(self) -> List[WeekdayCell]:
        cells = []
        cell_width = self.width / self.length
        for i in range(self.length):
            d = self.start + timedelta(i)
            if is_day_off(d, self.days_off, self.workdays):
                cell = DayOffWeekdayCell(d, cell_width, self.day_off_style)
            else:
                cell = WorkdayWeekdayCell(d, cell_width, self.workday_style)
            cells.append(cell)
        return cells
