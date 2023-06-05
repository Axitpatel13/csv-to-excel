import openpyxl
import sys
csv_name = input('Name: ')
sep = input('Sperator of the csv file')
excel_name = input('Name (output): ')
sheet_name = input('name (output):')
try:
    wb = openpyxl.load_workbook(excel_name)
    sheet = wb.get_sheet_by_name(sheet_name)
    file = open(csv_name, 'r', encoding='UTF-8')
except:
    print('file error')
    sys.exit()
row = 1
column=1
for line in file:
    line = line[:-1]
    line = line.split(sep)
    for data in line:
        sheet.cell(row,column).value = data
        column += 1    
    column = 1
    row += 1
wb.save(excel_name)
file.close()