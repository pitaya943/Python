# coding:utf-8
from openpyxl import Workbook
from openpyxl import load_workbook
from operator import itemgetter, attrgetter

fpath = 'myExcel.xlsx'
myWorkbook = load_workbook(fpath)

myWorktable = myWorkbook.get_sheet_by_name('sheet 1')

rows = myWorktable.rows
AllOfData = []

for row in list(rows):
    data = []
    for rowValue in row:
        data.append(rowValue.value)
    AllOfData.append(data)
    print(data)
print(AllOfData)

AllOfData_tuple = tuple(AllOfData)
sortedTuple = sorted(AllOfData_tuple, reverse=True, key=itemgetter(1))
sortedList = list(sortedTuple)
print(sortedList)

myWorktable2 = myWorkbook['sheet 2']
for detail in sortedList:
    myWorktable2.append(detail)

"""info = [
    ['name1', 40],
    ['name2', 26],
    ['name3', 89],
    ['name4', 30],
    ['name5', 98],
    ['name6', 88]
]

for detail in info:
    myWorktable.append(detail)"""


myWorkbook.save(fpath)
