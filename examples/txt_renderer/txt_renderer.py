from linum import Loader
from linum.txt_renderer.txt_renderer import TxtRenderer

DATA_PATH = "data.yaml"
CONTEXT_1_PATH = "context_1.yaml"
CONTEXT_2_PATH = "context_2.yaml"

# Add some tasks
tasks = Loader().load_tasks(DATA_PATH)

# Tasks for week
context = Loader().load_char_painter_context(CONTEXT_1_PATH)
tr = TxtRenderer(tasks, context)
print(tr.render())

# Tasks for 4 months
context = Loader().load_char_painter_context(CONTEXT_2_PATH)
tr = TxtRenderer(tasks, context)
print(tr.render())
