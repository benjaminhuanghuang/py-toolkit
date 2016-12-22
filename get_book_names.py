# -*- coding: utf-8 -*-

# http://springbible.fhl.net/Bible2/cgic201/Doc/abbreviation.html

import os
import io
import pyexcel
import json

MIN_DATA_ROW = 0
MAX_DATA_ROW = 66

excel = "/Users/hhuang/Documents/Links/Work/Python Scripts.xlsx"


sheet = pyexcel.get_sheet(file_name=excel, sheetname="Sheet1")

print "Processing..."# http://springbible.fhl.net/Bible2/cgic201/Doc/abbreviation.html

import os
import pyexcel
import json

MIN_DATA_ROW = 0
MAX_DATA_ROW = 66

excel = "/Users/hhuang/Documents/Links/Work/Python Scripts.xlsx"


sheet = pyexcel.get_sheet(file_name=excel, sheetname="Sheet1")


book_json = {}
for row in xrange(MIN_DATA_ROW, MAX_DATA_ROW):
    book_json[sheet.cell_value(row, 0)] = sheet.cell_value(row, 2)

book_json = {}
for row in xrange(MIN_DATA_ROW, MAX_DATA_ROW):
    print sheet.cell_value(row, 0)
    book_json[sheet.cell_value(row, 0)] = sheet.cell_value(row, 2)

json_file = "books.json"
home_dir = os.path.expanduser('~')
json_file_path = os.path.join(home_dir, "Desktop", json_file)

# Export json contains Chinese
with io.open(json_file_path, 'w', encoding='utf8') as txtfile:
    data = json.dumps(book_json, ensure_ascii=False)
    txtfile.write(unicode(data))
