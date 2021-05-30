from linum import SvgRenderer

renderer = SvgRenderer("tasks.yaml", "context.yaml")
renderer.render()
