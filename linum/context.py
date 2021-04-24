from datetime import date, timedelta


class Context:

    def __init__(self, **kwargs):
        self.cell_width = 3
        self.start_date = date.today()
        self.finish_date = date.today() + timedelta(7)
        self.inner_borders = True
        self.month_inner_borders = True
        self.left_border = True
        self.right_border = True
        self.months_in_row = 2

        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def length(self):
        return (self.finish_date - self.start_date).days

    @length.setter
    def length(self, length: int):
        self.finish_date = self.start_date + timedelta(max(length, 0))

    @property
    def year(self) -> None:
        return None

    @year.setter
    def year(self, year: int):
        self.start_date = date(year, 1, 1)
        self.finish_date = date(year + 1, 1, 1)
