from collections import OrderedDict
import pyexcel_ods as pe

sheet = pe.get_data("Spreadsheet3.ods")
products_per_suplier = {}

#calculate value of produts for each company
first_company_sum = 0
second_company_sum = 0
third_company_sum = 0

for row in sheet["Sheet1"]:
    for col in row:
        if col == "AAA Company":
            first_company_sum += row[1] * row [2]
        elif col == "BBB Company":
            second_company_sum += row[1] * row[2]
        elif col == "CCC Company":
            third_company_sum += row[1] * row [2]

print(f"Sum of AAA Company:", first_company_sum)
print(f"Sum of BBB Company:", second_company_sum)
print(f"Sum of CCC Company:", third_company_sum)

# file2 = OrderedDict()
# file2 = sheet
# file2.update({"Sheet2": [["row1","row2","row3"],[1,5,6]]})
# pe.save_data("Spreadsheet3.ods", file2)