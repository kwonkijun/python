import time
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from selenium import webdriver

driver = webdriver.Chrome() # 크롬 켜기
updater = Updater(token='1281403404:AAEW-knmZc14iyMsqNpNeMGTm0q-i8RH11o', use_context=True) # 봇의 업데이트 내용 받기 
dispatcher = updater.dispatcher # 봇의 행동 규칙 선언 

def pic(bot, update): # 봇의 행동 양식 
    for i in range(0,8):
        url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84'
        driver.get(url)
        time.sleep(2)
        title = driver.find_element_by_xpath("//div[@data-ellipsis-managed='{}']".format(i)).text.split('\n')[1]
        find = driver.find_element_by_xpath("//input[@title='검색어 입력']")
        find.clear()
        find.send_keys("영화 {}".format(title))
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        aud = driver.find_element_by_xpath("//dl[@class='r_grade']/dd[1]").text.split(' ')[0]
        cri = driver.find_element_by_xpath("//dl[@class='r_grade']/dd[3]").text.split(' ')[0]
        driver.find_element_by_xpath("//span[@class='thmb_v']").screenshot("D:/temp/poster.png")
        bot.send_message(chat_id=update.message.chat_id, text="네이버 영화 순위 {}위 : {}".format(i+1, title))
        bot.send_message(chat_id=update.message.chat_id, text="관람객 평점 : {}, 기자,평론가 평점 : {}".format(aud,cri))    
        bot.send_photo(chat_id=update.message.chat_id, photo=open("D:/temp/poster.png", 'rb')) # 사진 보내기 함수

pic_handler = CommandHandler('movie', pic) # 특정 업데이트(/movie)가 생길 때 그 반응으로 pic 수행
dispatcher.add_handler(pic_handler) # 봇의 행동 규칙으로 저장
updater.start_polling()  # 봇 구동