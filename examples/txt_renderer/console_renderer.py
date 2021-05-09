from linum.txt_renderer.console_renderer import ConsoleRenderer
from linum.txt_renderer.txt_renderer import TxtRenderer

DATA_PATH = "tasks.yaml"
CONTEXT_WEEK_PATH = "context_week.yaml"
CONTEXT_4_MONTHS_PATH = "context_4_months.yaml"

cr = ConsoleRenderer(DATA_PATH, CONTEXT_WEEK_PATH)
cr.render()

cr = ConsoleRenderer(DATA_PATH, CONTEXT_4_MONTHS_PATH)
cr.render()
