# 예제 10.3 일별로 일자, 시가, 고가, 저가, 종가, 거래량을 출력하는 코드

import win32com.client

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# SetInputValue
instStockChart.SetInputValue(0, "A003540")
# 개수로 요청하기 
instStockChart.SetInputValue(1, ord('2')) 
instStockChart.SetInputValue(4, 10)

# 기간으로 요청하기 
# instStockChart.SetInputValue(1, ord('1'))
# instStockChart.SetInputValue(2, 20161031)
# instStockChart.SetInputValue(3, 20161020)

instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetHeaderValue
numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

# GetDataValue
for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")