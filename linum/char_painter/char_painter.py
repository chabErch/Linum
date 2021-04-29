from typing import List

from linum import CharPainterContext
from linum import Composer
from linum import Task
from linum.char_painter.calendar import Calendar


class CharPainter:

    def __init__(self, tasks: List[Task] = None, context: CharPainterContext = CharPainterContext()):
        """
        Объект для рисования календаря символами.

        :param tasks:
        :param context:
        """
        self.context = context
        self.tasks = tasks or []

    def render(self):
        ll = Composer(self.tasks).safety_compose()
        c = Calendar(ll, self.context)
        return c.render()
