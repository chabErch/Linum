from datetime import date, timedelta


class Context:

    def __init__(self, **kwargs):
        self.start = date.today()
        self.finish = date.today() + timedelta(7)
        self.inner_borders = True
        self.month_inner_borders = True
        self.left_border = True
        self.right_border = True
        self.months_in_row = 2

        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def length(self):
        return (self.finish - self.start).days

    @length.setter
    def length(self, length: int):
        self.finish = self.start + timedelta(max(length, 0))

    @property
    def year(self) -> None:
        return None

    @year.setter
    def year(self, year: int):
        self.start = date(year, 1, 1)
        self.finish = date(year + 1, 1, 1)


class CharPainterContext(Context):

    def __init__(self, **kwargs):
        self.cell_width = 20
        super().__init__(**kwargs)
