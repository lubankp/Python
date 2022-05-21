from collections import OrderedDict
import pyexcel_ods as pe

sheet = pe.get_data("Desktop/Python kurs/Spreadsheet.ods")
print(sheet)

file2 = OrderedDict()
file2.update({"Sheet1": [[1,2,3],[1,5,6]]})
file2.update({"Sheet2": [["row1","row2","row3"],[1,5,6]]})
pe.save_data("Desktop/Python kurs/Spreadsheet2.ods", file2) 