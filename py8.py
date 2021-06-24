from collections import OrderedDict
import pyexcel_ods as pe

sheet = pe.get_data("Spreadsheet3.ods")
products_per_suplier = {}

#calculate how many products has each company
first_company = 0
second_company = 0
third_company = 0


for value in sheet.values():
    for row in value:

        if row[3] == "AAA Company:":
            first_company += 1
        elif row[3] == "BBB Company:":
            second_company += 1
        elif row[3] == "CCC Company:":
            third_company += 1

print(f"AAA Company", first_company, " ")
print(f"BBB Company", second_company, " ")
print(f"CCC Company", third_company, " ")

# file2 = OrderedDict()
# file2 = sheet
# file2.update({"Sheet2": [["row1","row2","row3"],[1,5,6]]})
# pe.save_data("Spreadsheet3.ods", file2)