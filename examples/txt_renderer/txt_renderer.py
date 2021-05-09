from linum.txt_renderer.txt_renderer import TxtRenderer

DATA_PATH = "tasks.yaml"
CONTEXT_WEEK_PATH = "context_week.yaml"
CONTEXT_4_MONTHS_PATH = "context_4_months.yaml"

# One week render
tr = TxtRenderer(DATA_PATH, CONTEXT_WEEK_PATH, "out_1.txt")
tr.render()

# 4 months render
tr = TxtRenderer(DATA_PATH, CONTEXT_4_MONTHS_PATH, "out_2.txt")
tr.render()
