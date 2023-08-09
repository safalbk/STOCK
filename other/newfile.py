import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
c1 = sheet.cell(row=1, column=2)
c1.value = 5
src='/storage/emulated/0/Download/a.xlsx'
wb.save(src)