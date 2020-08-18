from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

import pyautogui, pyperclip
import time
import telepot
import csv
from datetime import datetime

def product_name_check_func(string):
    words = string.split(' ')
    if(words[0] == words[1]):
        string = ' '.join(words[1:len(words)])

    words = string.split(' ')
    if(words[-1] == '코스트코'):
        string = ' '.join(words[0:len(words)-1])
    return string

def option_split_func (option):
    option = option.split(':')[1]
    option = option.split('/')[0]
    return option

_id = '7costco'
_pw = '0206coco'

driver = webdriver.Chrome()
url = "https://sell.smartstore.naver.com/#/login"
driver.implicitly_wait(3)
driver.get(url)

# 로그인
driver.find_element_by_css_selector("#loginId").click()
pyperclip.copy(_id)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
driver.find_element_by_css_selector("#loginPassword").click()
pyperclip.copy(_pw)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
driver.find_element_by_css_selector("#loginButton").click()

# 팝업창 처리
print(len(driver.find_elements_by_css_selector('.modal-dialog')))
if(len(driver.find_elements_by_css_selector('.modal-dialog')) > 0):
    driver.find_element_by_css_selector('#seller-content > div > div > div > div.modal-body > ncp-manager-notice-view > ng-transclude > button').click()
    time.sleep(1)

driver.find_element_by_css_selector('#seller-content > ui-view > div > div.seller-sub-content > div > div.panel-wrap.flex-col-6.flex-col-xs-12.order-md-1.order-xs-1 > div > div.panel-body.flex.flex-wrap > div.list-wrap.delivery-list.flex-col-6.flex-col-md-12 > div > ul > li:nth-child(1) > span.number-area > a').click()


# 프레임 전환하기
driver.switch_to.frame('__naverpay')
time.sleep(3)

# 500개 리스트 보기 
select = Select(driver.find_element_by_css_selector('.select._4LshyCrDpi'))
select.select_by_index(5)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.tui-grid-lside-area > div.tui-grid-body-area > div > div.tui-grid-table-container > table > tbody > tr > td.tui-grid-cell-row-head.tui-grid-cell")))
    print("element 찾기 완료", element.text)
except:
    print("element 찾기 실패")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table = soup.select_one('.tui-grid-rside-area > .tui-grid-body-area .tui-grid-table > tbody')
rows = table.select('tr')

products = []
cal_products = []

for i, row in enumerate(rows, 1):
    product_name = row.select_one('td:nth-child(15)').get_text()
    product_count = int(row.select_one('td:nth-child(19)').get_text())
    product_option = row.select_one('td:nth-child(17)').get_text()
    product_name = product_name_check_func(product_name)
    if(product_option != ''):
        product_option = option_split_func(product_option)
    products.append([product_name, product_count, product_option])


print(products)
#__app_root__ > div > div.napy_sub_content > div:nth-child(3) > div.npay_grid_area > div.grid > div.tui-grid-container > div.tui-grid-content-area.tui-grid-show-lside-area > div.tui-grid-rside-area > div.tui-grid-body-area > div > div.tui-grid-table-container > table > tbody > tr > td:nth-child(15)

"""
# 페이징 처리 
pageSize = len(driver.find_elements(By.CSS_SELECTOR, ".paggingnum")) + 1

products = []
cal_products = []

for i in range(pageSize):
    if i > 0 :
        driver.find_elements(By.CSS_SELECTOR, ".paggingnum")[i-1].click()
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sb-grid-results > tr.even")))
            print("element 찾기 완료", element.text)
        except:
            print("element 찾기 실패")
    # BeautifulSoup 과 연동
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.select('.sb-grid-results')[1] # 두개 grid 중 첫 번째
    rows = table.select('tr')

    for i, row in enumerate(rows, 1):
        product_name = row.select_one('td:nth-child(7)').get_text()
        product_count = int(row.select_one('td:nth-child(8)').get_text())
        product_option = row.select_one('td:nth-child(9)').get_text()
        product_name = product_name_check_func(product_name)
        if(product_option != ''):
            product_option = option_split_func(product_option)
        products.append([product_name, product_count, product_option])

# 상품 수량 계산
for product in products:
	exist = False
	for cal_product in cal_products:
		if(product[0] == cal_product[0] and product[2] == cal_product[2]):
			cal_product[1] += product[1]
			exist = True
	if(exist is False):
		cal_products.append(product)

print(cal_products)

f = open('결과.csv', 'w', encoding='CP949', newline='')  
csvWriter = csv.writer(f)
for i in cal_products:
    csvWriter.writerow(i)

f.close()
"""