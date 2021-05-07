from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet

from linum import LayerList
from linum.context import ExcelRendererContext
from linum.excel_renderer.calendar.header.header import Header


class Calendar:

    def __init__(self, layer_list: LayerList, context: ExcelRendererContext):
        self.context = context
        self.layer_list = layer_list

    def render(self, row: int, column: int, worksheet: Worksheet, workbook: Workbook):
        days_off = self.context.days_off
        workdays = self.context.workdays

        header_style = self.context.styles.get_sub_style("header")
        days_off_header_style = self.context.styles.get_sub_style("days_off").get_sub_style("header")
        header = Header(self.context.start, self.context.length, days_off, workdays,
                        header_style, days_off_header_style)
        header.render(row, column, worksheet, workbook)
