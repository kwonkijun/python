# 단기, 장기매수한계저가 구하는 프로그램

import sys
import time
from ctypes import *
from array import *
import win32com.client
import os
from datetime import datetime
import math

global maesu,stckmst,env1,order1,order,cnt,fd,counter,cputil,sell_flag,jongmok_su,maedo_mechegul
global account,cancel,cancel1,conclusion,cptd,maesu_danga,sonik_danga,temp,min_temp,cptd_new5331b
type_6033=["종목명","신용구분","대출일","결제잔고수량","결제장부단가","전일체결수량",
           "금일체결수량","체결잔고수량","","평가금액","평가손익","수익율","종목코드",
           "주문구분","","매도가능수량","만기일","체결장부가","손익단가"]
cnt = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
maesu_danga =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#종목수가 늘어나면 늘어난다
sonik_danga =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#종목수 만큼의 크기:동적할당 고민??
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#동적할당 안될까?
sell_flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
min_temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
maedo_mechegul = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#maesu=[10,13,17,22,30,36,45,54,65,77,90,103,118,134,151,168,186,206,226,247]
maesu=[10,10,20,20,30,40,50,50,70,80,90,100,120,130,150,170,190,210,230,250]
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

#fd = open('d:\data.txt','a+')
tes1 = env1.TradeInit(0)
if tes1 !=0:
    print(tes1,"bye!")
    sys.exit()
print("connected\n")

p_time=time.time()
print(p_time)#
c_time=time.ctime()
print(c_time)
#잔고 읽는법 
account1.SetInputValue(0,str(env1.AccountNumber[0]))#로그인한계좌 
account1.SetInputValue(1,'2')#상품관리구분 코드
account1.SetInputValue(2,50)
account1.BlockRequest()

stock_code_list = ["A033160", "A000430", "A267260", "A054950", "A006340", "A068790", "A040160", "A219420", "A000490", "A013570"]


#######################현재가 구하기######################################

for stock_code in stock_code_list: 
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
            #11은 현재가를 나타 내라는 말이고        
    print("현재가:",current_price)

    ##########################################################
    k=121#받아오는 데이터 개수 다른말로 몇일 데이타이냐 는 말이다.

    chart2.SetInputValue(0,code)#종목코드
    chart2.SetInputValue(1,ord('D'))
    chart2.SetInputValue(3,k)
    chart2.SetInputValue(4,'0')
    chart2.BlockRequest()
    jonga_list=[]
    goga_list=[]
    gega_list=[]
    dungrok_list=[]
    dungrokrul_list=[]
    a_list=[]
    jinpok_list=[]

    current_list=[]
    current_list_60=[]
    current_list_20=[]
    current_list_10=[]
    k_goga_list=[]
    k_gega_list=[]


    for i in range(k):
        value = chart2.GetDataValue (0,i)
        jonga = chart2.GetDataValue (4,i)#종가
        goga = chart2.GetDataValue (2,i)#고가
        gega = chart2.GetDataValue (3,i)#저가
        dungrok = chart2.GetDataValue (6,i)#등락

        jinpok=goga-gega

        jonga_list.append(jonga)
        goga_list.append(goga)
        gega_list.append(gega)
        dungrok_list.append(dungrok)
        jinpok_list.append(jinpok)
        
    print("종가리스트:",jonga_list)

    #print("고가리스트:",goga_list)

    #print("저가리스트:",gega_list)

    #print("등락리스트:",dungrok_list)

    #print("진폭리스트:",jinpok_list)
    print("등락률리스트:",dungrokrul_list)

    #print("고가중최고가",max(goga_list))
    #print("저가중최저가",min(gega_list))
    #print("종가합계",sum(jonga_list))

    #print("진폭리스트합:",sum(jinpok_list))
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
    pung_120=sum(jonga_list[0:120])/120

    print(k,"120구간 평균이다. ",pung_120)



    pung_60=sum(jonga_list[0:60])/60

    print(k,"60구간 평균이다. ",pung_60)



    pung_20=sum(jonga_list[0:20])/20

    print(k,"20구간 평균이다. ",pung_20)


    pung_10=sum(jonga_list[0:10])/10

    print(k,"10구간 평균이다. ",pung_10)

    print(jonga_list[0:10])

    
