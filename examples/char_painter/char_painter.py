from linum import Loader
from linum.char_painter import CharPainter

DATA_PATH = "data.yaml"
CONTEXT_1_PATH = "context_1.yaml"
CONTEXT_2_PATH = "context_2.yaml"

# Add some tasks
tasks = Loader().load_tasks(DATA_PATH)

# Tasks for week
context = Loader().load_char_painter_context(CONTEXT_1_PATH)
cp = CharPainter(tasks, context)
print(cp.render())

# Tasks for 4 months
context = Loader().load_char_painter_context(CONTEXT_2_PATH)
cp = CharPainter(tasks, context)
print(cp.render())
