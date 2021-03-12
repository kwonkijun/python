import os, sys, ctypes
import win32com.client
import pandas as pd
from datetime import datetime
import time, calendar

# 크레온 플러스 공통 OBJECT
cpCodeMgr = win32com.client.Dispatch('CpUtil.CpStockCode')
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
cpStock = win32com.client.Dispatch('DsCbo1.StockMst')
cpOhlc = win32com.client.Dispatch('CpSysDib.StockChart')
cpBalance = win32com.client.Dispatch('CpTrade.CpTd6033')
cpCash = win32com.client.Dispatch('CpTrade.CpTdNew5331A')
cpOrder = win32com.client.Dispatch('CpTrade.CpTd0311') 

def printlog(message, *args):
    """인자로 받은 문자열을 파이썬 셸에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *args)

def check_creon_system():
    """크레온 플러스 시스템 연결 상태를 점검한다."""
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        printlog('check_creon_system() : admin user -> FAILED')
        return False
 
    # 연결 여부 체크
    if (cpStatus.IsConnect == 0):
        printlog('check_creon_system() : connect to server -> FAILED')
        return False
 
    # 주문 관련 초기화 - 계좌 관련 코드가 있을 때만 사용
    if (cpTradeUtil.TradeInit(0) != 0):
        printlog('check_creon_system() : init trade -> FAILED')
        return False
    return True

def get_current_price(code):
    """인자로 받은 종목의 현재가, 매수호가, 매도호가를 반환한다."""
    cpStock.SetInputValue(0, code)  # 종목코드에 대한 가격 정보
    cpStock.BlockRequest()
    item = {}
    item['cur_price'] = cpStock.GetHeaderValue(11)   # 현재가
    item['ask'] =  cpStock.GetHeaderValue(16)        # 매수호가
    item['bid'] =  cpStock.GetHeaderValue(17)        # 매도호가    
    return item['cur_price'], item['ask'], item['bid']

def get_current_cash():
    """증거금 100% 주문 가능 금액을 반환한다."""
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]    # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    cpCash.SetInputValue(0, acc)              # 계좌번호
    cpCash.SetInputValue(1, accFlag[0])      # 상품구분 - 주식 상품 중 첫번째
    cpCash.BlockRequest() 
    return cpCash.GetHeaderValue(9) # 증거금 100% 주문 가능 금액

def get_stock_balance(code):
    """인자로 받은 종목의 종목명과 수량을 반환한다."""
    cpTradeUtil.TradeInit()
    acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
    accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체, 1:주식, 2:선물/옵션
    cpBalance.SetInputValue(0, acc)         # 계좌번호
    cpBalance.SetInputValue(1, accFlag[0])  # 상품구분 - 주식 상품 중 첫번째
    cpBalance.SetInputValue(2, 50)          # 요청 건수(최대 50)
    cpBalance.BlockRequest()     
    if code == 'ALL':
        printlog('계좌명: ' + str(cpBalance.GetHeaderValue(0)))
        printlog('결제잔고수량 : ' + str(cpBalance.GetHeaderValue(1)))
        printlog('평가금액: ' + str(cpBalance.GetHeaderValue(3)))
        printlog('평가손익: ' + str(cpBalance.GetHeaderValue(4)))
        printlog('종목수: ' + str(cpBalance.GetHeaderValue(7)))
    stocks = []
    for i in range(cpBalance.GetHeaderValue(7)):
        stock_code = cpBalance.GetDataValue(12, i)  # 종목코드
        stock_name = cpBalance.GetDataValue(0, i)   # 종목명
        stock_qty = cpBalance.GetDataValue(15, i)   # 수량
        if code == 'ALL':
            printlog(str(i+1) + ' ' + stock_code + '(' + stock_name + ')' 
                + ':' + str(stock_qty))
            stocks.append({'code': stock_code, 'name': stock_name, 
                'qty': stock_qty})
        if stock_code == code:  
            return stock_name, stock_qty
    if code == 'ALL':
        return stocks
    else:
        stock_name = cpCodeMgr.CodeToName(code)
        return stock_name, 0

def buy_stock(code):
    try:
        global bought_list      # 함수 내에서 값 변경을 하기 위해 global로 지정
        if code in bought_list: # 매수 완료 종목이면 더 이상 안 사도록 함수 종료
            #printlog('code:', code, 'in', bought_list)
            return False

        current_price, ask_price, bid_price = get_current_price(code)
        buy_qty = 0        # 매수할 수량 초기화
        if ask_price > 0:  # 매수호가가 존재하면   
            buy_qty = buy_amount // ask_price  
        printlog("매수수량 :", buy_qty)
        stock_name, stock_qty = get_stock_balance(code)  # 종목명과 보유수량 조회
        printlog("종목명:", stock_name)
        printlog("보유수량:", stock_qty)

        cpTradeUtil.TradeInit(0)
        acc = cpTradeUtil.AccountNumber[0]      # 계좌번호
        accFlag = cpTradeUtil.GoodsList(acc, 1) # -1:전체,1:주식,2:선물/옵션                
        # 최유리 FOK 매수 주문 설정
        cpOrder.SetInputValue(0, "2")        # 2: 매수
        cpOrder.SetInputValue(1, acc)        # 계좌번호
        cpOrder.SetInputValue(2, accFlag[0]) # 상품구분 - 주식 상품 중 첫번째
        cpOrder.SetInputValue(3, code)       # 종목코드
        cpOrder.SetInputValue(4, 1)    # 매수할 수량
        cpOrder.SetInputValue(5, 54000)
        cpOrder.SetInputValue(7, "0")        # 주문조건 0:기본, 1:IOC, 2:FOK
        cpOrder.SetInputValue(8, "01")       # 주문호가 1:보통, 3:시장가
                                                # 5:조건부, 12:최유리, 13:최우선 
        # 매수 주문 요청
        ret = cpOrder.BlockRequest() 
        printlog('최유리 FoK 매수 ->', stock_name, code, buy_qty, '->', ret)
        if ret == 4:
            remain_time = cpStatus.LimitRequestRemainTime
            printlog('주의: 연속 주문 제한에 걸림. 대기 시간:', remain_time/1000)
            time.sleep(remain_time/1000) 
            return False
        time.sleep(2)
        printlog('현금주문 가능금액 :', buy_amount)
        stock_name, bought_qty = get_stock_balance(code)
        printlog('get_stock_balance :', stock_name, stock_qty)
        if bought_qty > 0:
            bought_list.append(code)
            dbgout("`buy_etf("+ str(stock_name) + ' : ' + str(code) + 
                ") -> " + str(bought_qty) + "EA bought!" + "`")
    except Exception as ex:
        printlog(f"buy stock {code} exception! {ex}")

if __name__ == '__main__': 
    try:
        # CJ대한통운,대상우, 조광피혁, 풀무원, 해태제과식품
        # symbol_list = ['A000120', 'A001685', 'A004700', 'A017810', 'A101530']
        symbol_list = ['A004700']
        bought_list = []     # 매수 완료된 종목 리스트
        target_buy_count = 1 # 매수할 종목 수
        buy_percent = 0.2   
        printlog('check_creon_system() :', check_creon_system())  # 크레온 접속 점검
        stocks = get_stock_balance('ALL')      # 보유한 모든 종목 조회
        total_cash = int(get_current_cash())*0.25   # 100% 증거금 주문 가능 금액 조회 (현금 75% 유지)
        buy_amount = total_cash * buy_percent  # 종목별 주문 금액 계산
        printlog('100% 증거금 주문 가능 금액의 25% :', total_cash)
        printlog('종목별 주문 비율 :', buy_percent)
        printlog('종목별 주문 금액 :', buy_amount)
        printlog('시작 시간 :', datetime.now().strftime('%m/%d %H:%M:%S'))
        soldout = False

        while True:
            t_now = datetime.now()
            t_9 = t_now.replace(hour=9, minute=0, second=0, microsecond=0)
            t_start = t_now.replace(hour=9, minute=5, second=0, microsecond=0)
            t_sell = t_now.replace(hour=15, minute=15, second=0, microsecond=0)
            t_exit = t_now.replace(hour=15, minute=20, second=0,microsecond=0)
            today = datetime.today().weekday()
            if today == 5 or today == 6:  # 토요일이나 일요일이면 자동 종료
                printlog('Today is', 'Saturday.' if today == 5 else 'Sunday.')
                sys.exit(0)
            if t_start < t_now < t_sell :  # AM 09:05 ~ PM 03:15 : 매수
                for sym in symbol_list:
                    if len(bought_list) < target_buy_count:
                        buy_stock(sym)
                        time.sleep(1)
                if t_now.minute == 30 and 0 <= t_now.second <= 5: 
                    get_stock_balance('ALL')
                    time.sleep(5)
            if t_exit < t_now:  # PM 03:20 ~ :프로그램 종료
                printlog('`self-destructed!`')
                sys.exit(0)
            time.sleep(3)
    except Exception as ex:
        printlog('`main -> exception! ' + str(ex) + '`')
    