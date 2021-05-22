import tkinter
from datetime import date
from typing import Optional, List

from svgwrite import Drawing

from linum.svg_renderer.base.style import Style
from linum.svg_renderer.calendar.header.day.days_row import DaysRow
from linum.svg_renderer.calendar.header.month.months_row import MonthsRow
from linum.svg_renderer.calendar.header.weekday.weekdays_row import WeekdaysRow


class Header:

    def __init__(self, start: date, length: int, width: Optional[float] = None,
                 header_style: Optional[Style] = None, days_off_header_style: Optional[Style] = None,
                 days_off: Optional[List[date]] = None, workdays: Optional[List[date]] = None):
        self.width = width or tkinter.Tk().winfo_screenwidth()

        self.start = start
        self.length = length

        self.days_off_header_style = days_off_header_style or Style('default header')
        self.header_style = header_style or Style('default header')

        self.days_off = days_off or []
        self.workdays = workdays or []

    @property
    def height(self) -> int:
        wd_height = max(
            self.header_style.get_sub_style("days").get("width", 100),
            self.header_style.get_sub_style("weekdays").get("width", 100),
            self.header_style.get_sub_style("months").get("width", 100),
        )
        do_height = max(
            self.days_off_header_style.get_sub_style("days").get("width", 100),
            self.days_off_header_style.get_sub_style("weekdays").get("width", 100),
            self.days_off_header_style.get_sub_style("months").get("width", 100),
        )
        return max(wd_height, do_height)

    def render(self, drawing: Drawing, x: int, y: int):
        months_style = self.header_style.get_sub_style("months")
        mr = MonthsRow(self.start, self.length, self.width, months_style)

        days_style = self.header_style.get_sub_style("days")
        days_off_days_style = self.days_off_header_style.get_sub_style("days")
        dr = DaysRow(self.start, self.length, self.width,
                     days_style, days_off_days_style,
                     self.workdays, self.days_off)

        weekdays_style = self.header_style.get_sub_style("weekdays")
        days_off_weekdays_style = self.days_off_header_style.get_sub_style("weekdays")
        wr = WeekdaysRow(self.start, self.length, self.width,
                         weekdays_style, days_off_weekdays_style,
                         self.workdays, self.days_off)

        mr.render(drawing, x, y)
        dr.render(drawing, x, y + mr.height)
        wr.render(drawing, x, y + mr.height + dr.height)
