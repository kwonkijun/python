# 단기, 장기매수한계저가 구하는 프로그램

import sys
import time
from ctypes import *
from array import *
import win32com.client
import os
from datetime import datetime
import math
import openpyxl

# 엑셀읽기
workbook = openpyxl.load_workbook(r'C:\Users\스타트코딩\Desktop\재테크.xlsx')

# 시트 이름으로 불러오기
sheet = workbook['10장생']

stock_code_list = []

try:
    for i in range(4, 5000):
        if(type(sheet[f'C{i}'].value) != str):
            break;
        
        stock_code_list.append('A' + sheet[f'C{i}'].value)
except IndexError:
    pass

print(stock_code_list)

stckmst = win32com.client.Dispatch("dscbo1.StockMst")#현재가
env1 = win32com.client.Dispatch("CpTrade.CpTdUtil")#주문
order1 = win32com.client.Dispatch("CpTrade.CpTdNew9061")#예약주문
order = win32com.client.Dispatch("CpTrade.CpTd0311")#주문데이터
account = win32com.client.Dispatch("cptrade.CpTd6032")#가동중
#계좌 읽어오는 최신 버전
account1 = win32com.client.Dispatch("CpTrade.CpTd6033")#계좌별 잔고
cancel = win32com.client.Dispatch("CpTrade.CpTd0314")#취소주문
cancel1 = win32com.client.Dispatch("CpTrade.CpTdNew9064")#예약취소주문
check1 = win32com.client.Dispatch("CpTrade.CpTd9065")#예약주문현황
conclusion = win32com.client.Dispatch("dscbo1.CpConclusion")#주문에 대한체결현황
cptd = win32com.client.Dispatch("CpTrade.CpTd5342")#종목별 체결기준내역
cptd_5339 = win32com.client.Dispatch("CpTrade.CpTd5339")#종목별 미체결 잔량
cptd_new5331b = win32com.client.Dispatch("CpTrade.CpTdNew5331B")#매도주문 가능수량 조회
cputil = win32com.client.Dispatch("CpUtil.CpStockCode")#주식코드 조회작
cord_index = win32com.client.Dispatch("CpUtil.CpStockCode")#주식코드 조회작
chart = win32com.client.Dispatch("CpSysDib.StockChart")#주식코드 조회작
chart2 =win32com.client.Dispatch("Dscbo1.CbGraph1") 


for idx,stock_code in enumerate(stock_code_list, 1) : 
    time.sleep(0.5)
    stckmst.SetInputValue(0,stock_code)#0을 넣었으니 종목코드가  A005930으로 지정
            #삼성전자를 value로  지정 하는 과정이다는  말이다. 
    stckmst.BlockRequest()

    jongmok_name = stckmst.GetHeaderValue(1)
    print("종목이름:",jongmok_name)

    code = stckmst.GetHeaderValue(0)
    print("코드:",code)

    current_price = stckmst.GetHeaderValue(11)
    #위에서 삼성전자가 value로  지정됫고
    #11을 입력함으로써 삼성전자를  현재가를 데이터로 반환하라는 말이다 성공!!!
    print("현재가:",current_price)

    k=121#받아오는 데이터 개수 다른말로 몇일 데이타이냐 는 말이다.

    chart2.SetInputValue(0,code)#종목코드
    chart2.SetInputValue(1,ord('D'))
    chart2.SetInputValue(3,k)
    chart2.SetInputValue(4,'0')
    chart2.BlockRequest()
    jonga_list=[]
    goga_list=[]
    gega_list=[]
    a_list=[]
    jinpok_list=[]


    for i in range(k):
        value = chart2.GetDataValue (0,i)
        jonga = chart2.GetDataValue (4,i)#종가
        goga = chart2.GetDataValue (2,i)#고가
        gega = chart2.GetDataValue (3,i)#저가

        jinpok=goga-gega

        jonga_list.append(jonga)
        goga_list.append(goga)
        gega_list.append(gega)
        jinpok_list.append(jinpok)
        
    print("종가리스트:",jonga_list)
    pungun_jinpok=sum(jinpok_list)/k
    #print(A,"날동안평균진폭:",pungun_jinpok)
    #punggun_gaguk=sum(jonga_list)/len(jonga_list)
    #print(A,"날동안평균가격:",sum(jonga_list)/len(jonga_list))

    #한단 최저가 구하기 이가격을 벋어나면 매수 정지 해야 한다.
    #A일간 평균가격에서 평균진폭의 반을 뺴서 매수 하단을 구할수 있고
    #평균적으로 가능한 금액 이고
    #일반적으로 이가격에 갔다가 결국 상승 한다는 이야기이다. 
    long_mesuhange_gega=(sum(jonga_list)/len(jonga_list))-pungun_jinpok/2
    #print(k,"일간기준으로 장기매수한계저가",long_mesuhange_gega)

    #진폭 기준 현재가 부터 매수가능 저가 금액구하기
    #현재가 기준에서 수시로 하락 할수 있는 최저가이다.
    #현재가격에서 평균등락 폭의 반을 뺀다.
    short_mesuhange_gega=current_price-pungun_jinpok/2

    print(k,"일간기준으로 단기매수한계저가",short_mesuhange_gega)
    print(k,"일간기준으로 장기매수한계저가",long_mesuhange_gega)

    short_minus_long = (short_mesuhange_gega - long_mesuhange_gega)/short_mesuhange_gega
    long_minus_short = (long_mesuhange_gega - short_mesuhange_gega)/long_mesuhange_gega

    sheet[f'Q{idx + 3}'] = short_minus_long
    sheet[f'R{idx + 3}'] = long_minus_short

    if(short_minus_long > 0.06):
        print("고점")
        sheet[f'S{idx + 3}'] = "고점"

    if(short_minus_long < -0.10):
        print("저점이탈")
        sheet[f'S{idx + 3}'] = "저점이탈"
    if(abs(short_minus_long) < 0.03 and abs(long_minus_short) < 0.03):
        print("저가")
        sheet[f'S{idx + 3}'] = "저가"

    pung_120=sum(jonga_list[0:120])/120
    print(k,"120구간 평균이다. ",pung_120)

    pung_60=sum(jonga_list[0:60])/60
    print(k,"60구간 평균이다. ",pung_60)

    pung_20=sum(jonga_list[0:20])/20
    print(k,"20구간 평균이다. ",pung_20)

    pung_10=sum(jonga_list[0:10])/10
    print(k,"10구간 평균이다. ",pung_10)

    print(jonga_list[0:10])

    # 현재가
    sheet[f'F{idx + 3}'] = current_price

    # 단기매수한계저가
    sheet[f'O{idx + 3}'] = short_mesuhange_gega

    # 장기매수한계저가
    sheet[f'P{idx + 3}'] = long_mesuhange_gega

    workbook.save(r'C:\Users\스타트코딩\Desktop\재테크.xlsx')