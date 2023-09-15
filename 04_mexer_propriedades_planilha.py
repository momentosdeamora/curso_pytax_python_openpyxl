from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active

ws.sheet_properties.tabColor = "1072BA"
wb.save('primeira_planilha.xlsx')