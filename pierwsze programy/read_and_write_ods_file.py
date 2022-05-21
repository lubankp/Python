#calculate value of each kind of produts and write to file

from collections import OrderedDict
import pyexcel_ods as pe

sheet = pe.get_data("Spreadsheet3.ods")
sheet1 = sheet["Sheet1"]
for row in range(len(sheet1)):
    if row != 0 :
        raw5 = sheet1[row][1] * sheet1[row][2]
        sheet1[row].append(raw5)

file = OrderedDict()
file = sheet
pe.save_data("Spreadsheet3.ods", sheet)


