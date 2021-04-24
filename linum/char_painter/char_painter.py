from typing import List

from linum.char_painter.calendar.calendar import Calendar
from linum.composer import Composer
from linum.context import Context
from linum.task import Task


class CharPainter:

    def __init__(self, tasks: List[Task] = None, context: Context = Context()):
        self.context = context
        self.tasks = tasks or []

    def render(self):
        ll = Composer(self.tasks).safety_compose()
        c = Calendar(ll, self.context)
        return c.render()
