import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# 표 10.2 StockChart 클래스 요약
# 타입 (type)	입력 데이터의 종류	값 (value)
# 0	종목 코드	요청할 종목의 종목 코드
# 1	요청 구분	‘1’: 기간으로 요청, ‘2’: 갯수로 요청
# 2	요청종료일	YYYYMMDD 형식
# 3	요청시작일	YYYYMMDD 형식
# 4	요청개수	요청할 데이터의 개수
# 5	필드	0: 날짜, 1: 시간, 2: 시가, 3: 고가, 4: 저가, 5: 종가, 6: 전일대비, 8: 거래량, 9: 거래대금, 10: 누적체결매도수량
# 6	차트구분	‘D’: 일, ‘W’: 주, ‘M’: 월, ‘m’: 분, ‘T’: 틱
# 9	수정주가	‘0’: 무수정주가, ‘1’: 수정주가

instStockChart.SetInputValue(0, "A003540")
instStockChart.SetInputValue(1, ord('2')) # 문자열은 ord 함수로 아스키 코드로 변환해야 한다. 
instStockChart.SetInputValue(4, 10)
instStockChart.SetInputValue(5, 5)
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

instStockChart.BlockRequest()

numData = instStockChart.GetHeaderValue(3)
for i in range(numData):
    print(instStockChart.GetDataValue(0, i))