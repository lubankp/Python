from pyexcel_ods import get_data, save_data
from collections import OrderedDict

data = OrderedDict()
data.update({"Sheet1":[[1,2,3],[4,5,6]]})
data.update({"Sheet2":[["row1", "row2", "row3"]]})
save_data("Spreadsheet.ods", data)
