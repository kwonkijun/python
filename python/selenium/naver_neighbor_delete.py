from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import pyperclip
import time
import telepot
import datetime

driver = webdriver.Chrome(r'C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\selenium\chromedriver.exe')
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.implicitly_wait(3)
driver.get(url)
action = ActionChains(driver)

id ="kkj6369"
pw ="koC3848!!@"

time.sleep(2)

# 아이디 클립보드에서 COPY 후 입력
pyperclip.copy(id)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.TAB).perform()
time.sleep(2)
# 패스워드 클립보드에서 COPY 후 입력 
pyperclip.copy(pw)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()
time.sleep(2)

# 자동 로그인 등록하지 않음 버튼 클릭
driver.find_element_by_xpath('//*[@id="new.dontsave"]').click()
time.sleep(2)

# 블로그 이웃 관리 페이지 이동
url = 'https://admin.blog.naver.com/kkj6369/buddy/relation'
driver.get(url)

# 이웃관리 탭 클릭
driver.find_element_by_css_selector('#buddylist_config_anchor').click()

# iframe 이동
driver.switch_to.frame('papermain')
try:
    form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#buddyListManageForm")))
    print("element 찾기 완료")
except:
    print("element 찾기 실패")

neighbors = form.find_elements_by_css_selector('.tbl_buddymanage > tbody > tr')

delete_count = 0

for i, neighbor in enumerate(neighbors, 1):
	nickname = neighbor.find_element_by_css_selector('.ellipsis2').text
	last_update_date = neighbor.find_element_by_css_selector('td:nth-child(6)').text
	print(f'{i}. {nickname} {last_update_date}')

	isUpdated = True

	if(last_update_date != '-'):
		# 3달 이상 포스팅 안했을 경우 이웃 삭제
		publish_year = int('20' + last_update_date.split('.')[0])
		publish_mon = int(last_update_date.split('.')[1])
		date = datetime.datetime.today()
		now_year = date.year
		now_mon = date.month
		
		if(now_year == publish_year):
			if(now_mon - publish_mon >= 3):
				isUpdated = False
				print("삭제")
		else:
			isUpdated = False
			print("삭제")
	else:
		isUpdated = False
		print("삭제")	

	if(isUpdated == False):
		neighbor.find_element_by_css_selector('.checkwrap > input').click()
	time.sleep(0.5)

driver.