from linum.excel_renderer.excel_renderer import ExcelRenderer

er = ExcelRenderer("tasks.yaml", "context.yaml")
er.render()
