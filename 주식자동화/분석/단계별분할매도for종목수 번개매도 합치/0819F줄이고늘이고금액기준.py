#양이 많으면 적게 사도록 해놨음  1.장중매도 되면 더사고 매수되면 적게 산다. 
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
maesu_danga =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #종목수가 늘어나면 늘어난다
sonik_danga =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #종목수 만큼의 크기:동적할당 고민??
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #동적할당 안될까?
sell_flag = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
min_temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
maedo_mechegul = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#maesu=[10,13,17,22,30,36,45,54,65,77,90,103,118,134,151,168,186,206,226,247]
maesu=[10,10,20,20,30,40,50,50,70,80,90,100,120,130,150,170,190,210,230,250]
stckmst = win32com.client.Dispatch("dscbo1.StockMst") #현재가
env1 = win32com.client.Dispatch("CpTrade.CpTdUtil") #주문
order1 = win32com.client.Dispatch("CpTrade.CpTdNew9061") #예약주문
order = win32com.client.Dispatch("CpTrade.CpTd0311") #주문데이터
account = win32com.client.Dispatch("cptrade.CpTd6032") #가동중

#계좌 읽어오는 최신 버전
account1 = win32com.client.Dispatch("CpTrade.CpTd6033") #계좌별 잔고
cancel = win32com.client.Dispatch("CpTrade.CpTd0314") #취소주문
cancel1 = win32com.client.Dispatch("CpTrade.CpTdNew9064") #예약취소주문
check1 = win32com.client.Dispatch("CpTrade.CpTd9065") #예약주문현황
conclusion = win32com.client.Dispatch("dscbo1.CpConclusion") #주문에 대한체결현황
cptd = win32com.client.Dispatch("CpTrade.CpTd5342") #종목별 체결기준내역
cptd_5339 = win32com.client.Dispatch("CpTrade.CpTd5339") #종목별 미체결 잔량
cptd_new5331b = win32com.client.Dispatch("CpTrade.CpTdNew5331B") #매도주문 가능수량 조회
cputil = win32com.client.Dispatch("CpUtil.CpStockCode") #주식코드 조회작
limit_count = win32com.client.Dispatch("CpUtil.CpCybos") #주식코드 조회작

while True:
    #while를 사용하면 특정조건에서 명령을 무한히 수행한다. 
    #now=time.localtime()
    #if now.tm_hour==8 and now.tm_min>=21 :
    #while을 쓰므로써 특정 시간에 작동 시킬 수 있게 됬다   특정 시간이거나 특정 시간 사이에서 무한이 진행 한다.
        
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
        account1.SetInputValue(1,'10')#상품관리구분 코드
        account1.SetInputValue(2,50)
        account1.BlockRequest()

        print("\n")

        def Sell(code,surang,current_price):
                #매도가능수량 있는지 체크
            order.SetInputValue(0,'1')
            order.SetInputValue(1,str(env1.AccountNumber[0]))
            order.SetInputValue(2,'10')
            order.SetInputValue(3,code)
            order.SetInputValue(4,1)#maesu[self.Counter[index]])
            order.SetInputValue(5,current_price-5)
            order.SetInputValue(8,'10')#01:지정가 03:시장가
            ret = order.BlockRequest()
            if ret == 0:
                if order.GetDibStatus()==0:
                    print("매도주문정상")
                    return 1
                else:
                    print("매도주문실패",order.GetDibMsg1())
                    return 0

        C=gnago_jomoksu=account1.GetHeaderValue(7)
        print("잔고 종목수는",C)
        
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@첫번쨰종목 매도@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        for i in range(C):

                Limit_time= limit_count.LimitRequestRemainTime
                print("이시간동안 주문하마 안된다.",Limit_time)
                possi_jumun_line=limit_count.GetLimitRemainCount(0)#주문에 남은 라인이 몇개인가 
                print("주문또는 게좌요청하는데 남은라인",possi_jumun_line)
                possi_current_line=limit_count.GetLimitRemainCount(1)#계좌와 상관업는 현재가  남은 라인이 몇개인가 
                print("계좌와 상관업는 현재가  남은 라인",possi_current_line)

                if possi_jumun_line>5 and possi_current_line>0:
                        print("현재가라인 주문라인 유효 진행 한다.")
                else:
                                print("라인 부족인다. 잠시 정지한다.  ")
                                time.sleep(5)                

                time.sleep(1.5)
                
                value=account1.GetDataValue(0,i)
                print(i+1,"종목명:", value)

                suikrul=account1.GetDataValue(11,i)#지금 동휘계좌에 잔고40개정도라서 그이상에서는
                #그이상에서는 오류가 난다.
                #(11,0)은 11이 잔고 수익률을 보여 달라는 말이고  0은 잔고 멘위에 있는 것을
                #이야기 하고 있다. 
                print("수익률:" ,suikrul)

                sonik_danga=account1.GetDataValue(18,i)#매도 가능한 잔고 수량을 보여 달라는 이야기다.
                print("손익단가:",sonik_danga)

                surang=account1.GetDataValue(15,i)#매도 가능한 잔고 수량을 보여 달라는 이야기다.
                print("잔고수량:",surang)

                jango_kum=account1.GetDataValue(9,i)#종목에 잔고금액 얼마인가. 
                print("잔고금액:",jango_kum)

                code=account1.GetDataValue(12,i)
                print("종목코드:",code)

                stckmst.SetInputValue(0,code)#0을 넣었으니 종목코드가  A005930으로 지정
                #삼성전자를 value로  지정 하는 과정이다는  말이다. 
                stckmst.BlockRequest()

                current_price = stckmst.GetHeaderValue(11)
                #위에서 삼성전자가 value로  지정됫고
                #11을 입력함으로써 삼성전자를  현재가를 데이터로 반환하라는 말이다 성공!!!
                #11은 현재가를 나타 내라는 말이고 
                print("현재가:",current_price)

                medo_hoga = stckmst.GetHeaderValue(16)
                print("매도호가:",medo_hoga)

                b=1
                
                if surang < 4:
                    b=1
                if surang >= 4 and surang < 30:
                    b=3
                elif surang >= 30 and surang < 50:
                    b=5
                elif surang >= 50 and surang < 100:
                    b=11
                elif surang >= 100 and surang < 200:
                    b=22
                elif surang >= 200 and surang < 300:
                    b=33
                elif surang >= 300 :
                    b=55

                print("매도수량:",b)

                if  current_price < 1000:
                    a=1
                elif current_price >= 1000 and current_price < 5000:
                    a=5
                elif current_price >= 5000 and current_price < 10000:
                    a=10
                elif current_price >= 10000 and current_price < 50000:
                    a=50
                elif current_price >= 50000 and current_price < 100000:
                    a=100
                elif current_price >= 100000 and current_price < 1000000:
                    a=500
                
#@@@@@@@@@@@@@@@@@@@@@@@번개매도 하는곳

                if sonik_danga*1.003<current_price and surang>100 :

                        A=33#매도량
                        B=1#매도가격 간격
                        D=1#매도 간격 조절하기 
                        C=3#번개 분할매도 칸 혹은 매도 횟수 
                                        
                        print("매도량:", 1*A,1*A,2*A,1*A,1*A,1*A,1*A,1*A,2*A,2*A)

                        print("매도총량:", 1*A+1*A+2*A+1*A+1*A+1*A+1*A+1*A+2*A+2*A,"주")

                        medo_chongkum=current_price*(1*A+1*A+2*A+1*A+1*A+1*A+1*A+1*A+2*A+2*A)
                        print("1회 매도 총금액:",medo_chongkum)
                        print("매도금액 간격:", a*1*B*D,a*2*B*D,a*3*B*D,a*4*B*D,a*5*B*D,a*6*B*D,a*7*B*D,a*8*B*D,5*9*B*D,5*10*B*D)

                        #매수조건정의 
                        #매도짜기 첫번쨰 매도 

                        mesu_rang=[1*A,1*A,2*A,1*A,1*A,1*A,1*A,1*A,2*A,2*A,64,1]#매수량 리스트  ///2주 2주 4주 산다는 이야기다. 
                        print(mesu_rang[2])
                        mesu_kum=[2*B*D,3*B*D,4*B*D,4*B*D,5*B*D,6*B*D,7*B*D,8*B*D,9*B*D,10*B*D,1,1,1]#매도간격 금액 리스트  ///5
                        print(mesu_kum[5])

                        for i in range(C):#매수 횟수  ///를 결정한다.
                                time.sleep(1)
                                #매도짜기 두번째매도 
                                order.SetInputValue(0,'1')#(0주문코드,1매도 2.매수)
                                order.SetInputValue(1,str(env1.AccountNumber[0]))#계좌번호
                                order.SetInputValue(2,'10')
                                order.SetInputValue(3,code)#종목코드
                                order.SetInputValue(4,mesu_rang[i])#주문수량2주라는거
                                order.SetInputValue(5,current_price+a*mesu_kum[i])#주문가격
                                order.SetInputValue(8,'01')#01:지정가 03:시장가
                                order.BlockRequest()
                                time.sleep(0)
                                print("매도다")

                                time.sleep(3)      

                                Limit_time= limit_count.LimitRequestRemainTime
                                print("이시간동안 주문하마 안된다.",Limit_time)
                                possi_jumun_line=limit_count.GetLimitRemainCount(0)#주문에 남은 라인이 몇개인가 
                                print("주문또는 게좌요청하는데 남은라인",possi_jumun_line)
                                possi_current_line=limit_count.GetLimitRemainCount(1)#계좌와 상관업는 현재가  남은 라인이 몇개인가 
                                print("계좌와 상관업는 현재가  남은 라인",possi_current_line)

                                if possi_jumun_line>5 and possi_current_line>0:
                                    print("현재가라인 주문라인 유효 진행 한다.")
                                else:
                                    print("라인 부족인다. 잠시 정지한다.  ")
                                    time.sleep(5)

                b=1  
                if surang < 4:
                    b=1
                if surang >= 4 and surang < 30:
                    b=3
                elif surang >= 30 and surang < 50:
                    b=5
                elif surang >= 50 and surang < 100:
                    b=11
                elif surang >= 100 and surang < 200:
                    b=22
                elif surang >= 200 and surang < 300:
                    b=33
                elif surang >= 300 and surang < 400:
                    b=44
                elif surang >= 400 and surang < 500:
                    b=55
                elif surang >= 500 and surang < 600:
                    b=66
                elif surang >= 600 and surang < 700:
                    b=77
                elif surang >= 700 and surang < 800:
                    b=88
                elif surang >= 800 and surang < 900:
                    b=99
                elif surang >= 900 :
                    b=111

                print("매도수량:",b)
              
                if sonik_danga*1.003<current_price and surang<100:
                #동시에 매도 가능수량이 몇주 이상으로 정의 내리는 거 고려 해보자 
                    e=1.01
                  
                #매도짜기 첫번쨰쨰 매도 
                    order.SetInputValue(0,'1')#(0주문코드,1매도)
                    order.SetInputValue(1,str(env1.AccountNumber[0]))#계좌번호
                    order.SetInputValue(2,'10')
                    order.SetInputValue(3,code)#종목코드
                    order.SetInputValue(4,b)#주문수량2주라는거
                    order.SetInputValue(5,current_price)#주문가격
                    order.SetInputValue(8,'01')#01:지정가 03:시장가
                    order.BlockRequest()                    

                    print("@@@@@@@@@@@@@@@@@@@@@@@첫번분할매도다  짜짠@@@@@@@@@@@@@@@@@@@@@@@@@@")
                     
                else:
                    print("@수익권도달전이나 종목수미달  매도안한다@")

                print("\n")
                
                time.sleep(2)
        Limit_time= limit_count.LimitRequestRemainTime
        print("이시간동안 주문하마 안된다.",Limit_time)
        possi_jumun_line=limit_count.GetLimitRemainCount(0)#주문에 남은 라인이 몇개인가 
        print("주문또는 게좌요청하는데 남은라인",possi_jumun_line)
        possi_current_line=limit_count.GetLimitRemainCount(1)#계좌와 상관업는 현재가  남은 라인이 몇개인가 
        print("계좌와 상관업는 현재가  남은 라인",possi_current_line)
                                               
        time.sleep(1)