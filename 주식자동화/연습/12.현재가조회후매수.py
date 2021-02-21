import win32com.client
import time

class CpStockMst:
    def Request(self, code):
        # 연결 여부 체크
        objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
        bConnect = objCpCybos.IsConnect
        if (bConnect == 0):
            print("PLUS가 정상적으로 연결되지 않음. ")
            return False
        
        # 현재가 객체 구하기
        objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
        objStockMst.SetInputValue(0, code)  #종목 코드 
        objStockMst.BlockRequest()
        
        # 현재가 통신 및 통신 에러 처리 
        rqStatus = objStockMst.GetDibStatus()
        rqRet = objStockMst.GetDibMsg1()
        print("통신상태", rqStatus, rqRet)
        if rqStatus != 0:
            return False
        
        # 현재가 정보 조회
        code = objStockMst.GetHeaderValue(0)  #종목코드
        name= objStockMst.GetHeaderValue(1)  # 종목명
        time= objStockMst.GetHeaderValue(4)  # 시간
        cprice= objStockMst.GetHeaderValue(11) # 종가
        diff= objStockMst.GetHeaderValue(12)  # 대비
        open= objStockMst.GetHeaderValue(13)  # 시가
        high= objStockMst.GetHeaderValue(14)  # 고가
        low= objStockMst.GetHeaderValue(15)   # 저가
        offer = objStockMst.GetHeaderValue(16)  #매도호가
        bid = objStockMst.GetHeaderValue(17)   #매수호가
        vol= objStockMst.GetHeaderValue(18)   #거래량
        vol_value= objStockMst.GetHeaderValue(19)  #거래대금
        
        if cprice > 3935:
            print("==========매수가 아님=========")
        else:
            print("==========매수 진행===========")
            myCpTrade = MyCpTrade()
            if myCpTrade.order("2", code, 1, cprice):
                print("매수 완료")
        
        if cprice > 3940:
            myCpTrade = MyCpTrade()
            if myCpTrade.order("1", code, 1, cprice):
                print("매도 완료")

        # 예상 체결관련 정보
        exFlag = objStockMst.GetHeaderValue(58) #예상체결가 구분 플래그
        exPrice = objStockMst.GetHeaderValue(55) #예상체결가
        exDiff = objStockMst.GetHeaderValue(56) #예상체결가 전일대비
        exVol = objStockMst.GetHeaderValue(57) #예상체결수량
        
        
        print("코드", code)
        print("이름", name)
        print("시간", time)
        print("종가", cprice)
        print("대비", diff)
        print("시가", open)
        print("고가", high)
        print("저가", low)
        print("매도호가", offer)
        print("매수호가", bid)
        print("거래량", vol)
        print("거래대금", vol_value)
        
        
        if (exFlag == ord('0')):
            print("장 구분값: 동시호가와 장중 이외의 시간")
        elif (exFlag == ord('1')) :
            print("장 구분값: 동시호가 시간")
        elif (exFlag == ord('2')):
            print("장 구분값: 장중 또는 장종료")
        
        print("예상체결가 대비 수량")
        print("예상체결가", exPrice)
        print("예상체결가 대비", exDiff)
        print("예상체결수량", exVol)

class MyCpTrade:
    def order(self, type, code, amount, price):
        # 주문 초기화
        objTrade =  win32com.client.Dispatch("CpTrade.CpTdUtil")
        initCheck = objTrade.TradeInit(0)
        if (initCheck != 0):
            print("주문 초기화 실패")
            return False
        
        # 주식 매수 주문
        acc = objTrade.AccountNumber[0] #계좌번호
        accFlag = objTrade.GoodsList(acc, 1)  # 주식상품 구분
        print(acc, accFlag[0])
        objStockOrder = win32com.client.Dispatch("CpTrade.CpTd0311")
        objStockOrder.SetInputValue(0, type)   # 1: 매도 2: 매수
        objStockOrder.SetInputValue(1, acc )   #  계좌번호
        objStockOrder.SetInputValue(2, accFlag[0])   # 상품구분 - 주식 상품 중 첫번째
        objStockOrder.SetInputValue(3, code)   # 종목코드 - A004410 - 서울식품 종목
        objStockOrder.SetInputValue(4, amount)   # 매수수량 10주
        objStockOrder.SetInputValue(5, price)   # 주문단가  - 14,100원
        objStockOrder.SetInputValue(7, "0")   # 주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
        objStockOrder.SetInputValue(8, "01")   # 주문호가 구분코드 - 01: 보통
        
        # 매수 주문 요청
        objStockOrder.BlockRequest()
        
        rqStatus = objStockOrder.GetDibStatus()
        rqRet = objStockOrder.GetDibMsg1()
        print("통신상태", rqStatus, rqRet)
        if rqStatus != 0:
            return False

        return True
if __name__ == "__main__":
    CpMst = CpStockMst()
    while True:
        CpMst.Request('A114800')
        time.sleep(10)