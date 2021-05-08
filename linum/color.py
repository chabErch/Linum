import colorsys
import re
from typing import Union, Tuple
import wcag_contrast_ratio as contrast


class Color:

    def __init__(self, rgb: Union[str, int] = 0x000000):
        if isinstance(rgb, int):
            self.r = (rgb & 0xFF0000) >> 16
            self.g = (rgb & 0x00FF00) >> 8
            self.b = rgb & 0x0000FF
        elif isinstance(rgb, str) and re.fullmatch("#[0-9a-fA-F]{6}", rgb):
            self.r = int(rgb[1:3], 16)
            self.g = int(rgb[3:5], 16)
            self.b = int(rgb[5:7], 16)
        else:
            raise ValueError

    def __str__(self):
        return '#' + hex(self.rgb)[2:].zfill(6)

    def contrast(self, color: 'Color') -> float:
        return contrast.rgb(self.r_g_b_percents, color.r_g_b_percents)

    @property
    def rgb(self) -> int:
        r, g, b = self.r_g_b
        r = r << 16
        g = g << 8
        return r + g + b

    @property
    def r_g_b(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    @property
    def r_g_b_percents(self) -> Tuple[float, float, float]:
        r, g, b = self.r_g_b
        return r / 255, g / 255, b / 255

    @property
    def h_s_v_percents(self) -> Tuple[float, float, float]:
        """
        Converts color to hue, saturation and value parts in percents.

        :return: Tuple[float, float, float]
        """
        r, g, b = self.r_g_b_percents
        return colorsys.rgb_to_hsv(r, g, b)

    @staticmethod
    def from_h_s_v_percents(h: float, s: float, v: float) -> 'Color':
        """
        Converts hue, saturation and value parts in percents to rgb int value.

        :param h: hue part in percents
        :param s: saturation part in percents
        :param v: value part in percents
        :return: int
        """
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b, = int(r * 255), int(g * 255), int(b * 255)

        r = r << 16
        g = g << 8
        return Color(r + g + b)

