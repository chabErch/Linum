from datetime import date

from linum.char_painter import CharPainter
from linum.context import Context
from linum.task import Task

# Add some tasks
tasks = [
    Task('Vacation', date(2020, 1, 2), 20),

    Task('Duty', date(2020, 2, 1), 2),
    Task('Duty', date(2020, 2, 7), 2),
    Task('Duty', date(2020, 2, 15), 2),
    Task('Duty', date(2020, 2, 25), 2),

    Task('Task #1', date(2020, 1, 22), 10),
    Task('Task #2', date(2020, 2, 3), 10),
    Task('Task #3', date(2020, 2, 23), 10),
    Task('Task #4', date(2020, 3, 17), 10),

    Task('Current day task', length=5)
]

# Initial context
c = Context()

# Tasks for week
cp = CharPainter(tasks, c)
print(cp.render())

# Tasks for 4 months
c.start_date = date(2020, 1, 1)
c.finish_date = date(2020, 5, 1)
c.inner_borders = False
c.month_inner_borders = True
cp = CharPainter(tasks, c)
print(cp.render())

