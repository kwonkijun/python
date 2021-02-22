import openpyxl
from openpyxl.chart import Reference, Series, BarChart

book = openpyxl.load_workbook(r"C:\Users\스타트코딩\Desktop\main\python\업무자동화\엑셀자동화\엑셀예제\2017년_광고비_LG전자.xlsx")
sheet = book.active

chart = BarChart()
chart.title = "LG전자 월별 광고비"
Reference(sheet, range_string="Sheet1!C2:C13")