from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active

ws.title = "Minha planilha"
print(ws.title)