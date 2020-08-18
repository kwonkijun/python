from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

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
url = "https://www.esmplus.com/"
driver.implicitly_wait(3)
driver.get(url)

# 로그인
driver.find_element_by_css_selector("#rdoSiteSelect").click()
time.sleep(1)
driver.find_element_by_css_selector("#SiteId").send_keys(_id)
time.sleep(1) 
driver.find_element_by_css_selector("#SitePassword").send_keys(_pw)
time.sleep(1)
driver.find_element_by_css_selector("#btnSiteLogOn").click()


# 팝업창 처리
# Show all windows
allhandles = driver.window_handles
print(f'Total {allhandles} windows has been opened.')
# Switch last open window
if(len(allhandles) > 1):
    for handle in allhandles:
        driver.switch_to.window(handle)
        myurl = driver.current_url     
        print(f"Focused window's url is {myurl} ")

        if 'http://www.esmplus.com/Home' not in myurl:
            print(f"===close window's {myurl}===")
            driver.close()
        time.sleep(1)
    # 팝업창을 끈 후 다시 원래 사이트로 돌아와야 됨.
    driver.switch_to.window(allhandles[0]) 

# 프레임 전환하기
driver.switch_to.frame('ifm_contents')
time.sleep(1)
driver.find_elements_by_css_selector('.sales_status_number > a')[2].click()
time.sleep(1)
driver.switch_to_default_content()
driver.switch_to.frame('ifm_TDM106')
time.sleep(1)
driver.switch_to.frame('ifm_contents1')

# 500개 리스트 보기 
select = Select(driver.find_element_by_id('selPagingSize'))
select.select_by_value('500')

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".sb-grid-results > tr.even")))
    print("element 찾기 완료", element.text)
except:
    print("element 찾기 실패")

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
