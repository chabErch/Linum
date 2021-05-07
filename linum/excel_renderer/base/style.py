from typing import List

from xlsxwriter import Workbook
from xlsxwriter.format import Format

from linum.helper import color_to_str, add_blackout

WHITE_COLOR = 0xFFFFFF


class Style(dict):

    def __init__(self, **kwargs):
        """
        Container for styles settings.

        :param kwargs: styles settings
        """
        self.parents: List[Style] = []
        super().__init__(**kwargs)

    def get(self, key, default=None):
        """
        Overridden method. Search key among self and parents styles.

        :param key: key to search
        :param default: default value to return
        :return:
        """
        value = super().get(key, None)
        if value is not None:
            return value
        else:
            if not self.parents:
                return default
            else:
                value = None
                for parent in self.parents:
                    v = parent.get(key)
                    value = v if v is not None else value
                return value if value is not None else default

    def get_sub_style(self, key) -> 'Style':
        """
        Return sub style if exist, else create new sub style.

        :param key: key for sub style
        :return: Style
        """
        if key in self and isinstance(self[key], Style):
            return self[key]
        sub_style = Style()
        sub_style.parents = [self]
        return sub_style

    @property
    def all(self) -> dict:
        """
        Returns all style params including inherited.

        :return: dict
        """
        d = {}
        for k, v in self.items():
            if not isinstance(v, dict):
                d.update({k: v})

        d_ = {}
        for parent in self.parents:
            d_.update(parent.all)

        d_.update(d)
        return d_

    def get_xlsxwriter_format(self, workbook: Workbook) -> Format:
        """
        Gets xlsxwriter format object.

        :param workbook:
        :return:
        """
        style_params = self.all

        # Applying blackout
        if self.get("use_blackout", False):
            blackout_value = self.get("blackout_value", 0.12)
            style_params = self.apply_blackout(style_params, blackout_value)

        # Fixing colors
        style_params = self.fix_colors(style_params)

        format_ = workbook.add_format()
        for k, v in style_params.items():
            try:
                getattr(format_, "set_" + k)(v)
            except AttributeError:
                pass
        return format_

    @staticmethod
    def fix_colors(style_dict: dict):
        """
        It fixes colors to use them with xlsxwriter lib.

        """
        for k, v in style_dict.items():
            if k.find("color") > -1:
                style_dict.update({k: color_to_str(v)})
        return style_dict

    @staticmethod
    def apply_blackout(style_dict: dict, blackout_value: float):
        """
        Applies blackout to all colors in style dict

        """
        style_dict.setdefault('bg_color', WHITE_COLOR)
        for k, v in style_dict.items():
            if k.find("color") > -1:
                style_dict[k] = add_blackout(v, blackout_value)
        return style_dict
