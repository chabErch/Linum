from typing import Optional, List
from uuid import uuid4

from svgwrite import Drawing
from svgwrite.masking import ClipPath
from svgwrite.path import Path
from svgwrite.shapes import Rect
from svgwrite.text import Text

from linum.svg_renderer.base.style import Style


class Cell:

    def __init__(self, content: str = "", width: float = 100.0, style: Optional[Style] = None,
                 extra_classes: Optional[List[str]] = None):
        self.content = content
        self.width = width
        self.style = style or Style()

        self._extra_classes = extra_classes or []

    @property
    def height(self) -> int:
        return self.style.get("height", 100)

    @classmethod
    def get_class(cls) -> str:
        return "cell"

    @classmethod
    def get_classes(cls) -> List[str]:
        c = cls
        l = [c.get_class()]
        while c is not Cell:
            c = c.__bases__[0]
            l.insert(0, c.get_class())
        return l

    def render(self, drawing: Drawing, x: int, y: int):
        # Background
        bg_style = self.style.get_sub_style("background")
        bg_height = bg_style.get("height", self.height)
        bg_style.update({"height": None, "width": None, "x": None, "y": None})
        bg_classes = " ".join(self.get_classes() + self._extra_classes + ["background"])
        background = Rect(insert=(x, y), size=(self.width, bg_height),
                          class_=bg_classes, debug=False, style=bg_style.get("style", ""))
        drawing.add(background)

        # Clip mask
        id_ = uuid4().hex
        clip_path_style = " ".join(self.get_classes() + self._extra_classes + ["clip-mask"])
        clip_path = ClipPath(style=clip_path_style, id=id_)
        clip_path.add(background)
        drawing.add(clip_path)

        # Text
        text_style = self.style.get_sub_style("text")
        text_classes = " ".join(self.get_classes() + self._extra_classes + ["text"])

        # Setting text align
        align = text_style.get("align", "center")
        if align == "left":
            tx = x
        elif align == "center":
            tx = x + self.width / 2
        elif align == "right":
            tx = x + self.width
        else:
            msg = "Incorrect align value for cell: '{}'".format(align)
            raise ValueError(msg)

        # Setting text valign
        valign = text_style.get("valign", "vcenter")
        if valign == "top":
            ty = y
        elif valign == "vcenter":
            ty = y + bg_height / 2
        elif valign == "bottom":
            ty = y + bg_height
        else:
            msg = "Incorrect valign value for cell: '{}'".format(valign)
            raise ValueError(msg)

        # Text rendering
        text = Text(self.content, insert=(tx, ty), class_=text_classes, debug=False,
                    style=text_style.get("style", ""), clip_path="url(#{})".format(id_))
        drawing.add(text)

        # Borders
        borders_style = self.style.get_sub_style("border")
        border_classes = self.get_classes() + self._extra_classes + ["border"]

        # Left border
        l_border_style = borders_style.get_sub_style("left")
        l_border_height = l_border_style.get("height", bg_height)
        l_border_style.update({"x": None, "y": None, "height": None})
        if l_border_style.get("left", False):
            l_border_style.update({"left": None})
            l_border_classes = " ".join(border_classes + ["left"])
            l_border_style.update({"class_": l_border_classes})
            l_border = Path(["M", x, y, "L", x, y + l_border_height],
                            class_=l_border_classes,
                            style=l_border_style.get("style", '""'))
            drawing.add(l_border)

        # Right border
        r_border_style = borders_style.get_sub_style("right")
        r_border_height = l_border_style.get("height", bg_height)
        r_border_style.update({"x": None, "y": None, "height": None})
        if r_border_style.get("right", False):
            r_border_style.update({"right": None})
            r_border_classes = " ".join(border_classes + ["right"])
            r_border_style.update({"class_": r_border_classes})
            r_border = Path(["M", x + self.width, y, "L", x + self.width, y + r_border_height],
                            class_=r_border_classes,
                            style=r_border_style.get("style", '""'))
            drawing.add(r_border)

        # Top border
        t_border_style = borders_style.get_sub_style("top")
        t_border_style.update({"x": None, "y": None, "height": None})
        if t_border_style.get("top", False):
            t_border_style.update({"top": None})
            t_border_classes = " ".join(border_classes + ["top"])
            t_border_style.update({"class_": t_border_classes})
            t_border = Path(["M", x, y, "L", x + self.width, y],
                            class_=t_border_classes,
                            style=t_border_style.get("style", '""'))
            drawing.add(t_border)

        # Bottom border
        b_border_style = borders_style.get_sub_style("bottom")
        b_border_style.update({"x": None, "y": None, "height": None})
        if b_border_style.get("bottom", False):
            b_border_style.update({"bottom": None})
            b_border_classes = " ".join(border_classes + ["bottom"])
            b_border_style.update({"class_": b_border_classes})
            b_border = Path(["M", x, y + l_border_height, "L", x + self.width, y + r_border_height],
                            class_=b_border_classes,
                            style=b_border_style.get("style", '""'))
            drawing.add(b_border)

        drawing.save(pretty=True)
