#댓글 버튼 #content > section > div.list_post_article.list_post_article_comments > div:nth-child(7) > div > div.info_post > div.comments > a:nth-child(2)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from my_modules import reply_maker
import pyperclip , pyautogui
import time
import telepot

driver = webdriver.Chrome()
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

# 블로그 홈으로 이동

page_num = 1 # 페이지 번호 
max_page_num = 10 # 페이지 당최대 이웃 새글 수 
url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
driver.get(url)
time.sleep(1)

# 답글 버튼이 생기기 까지 기다리는 코드 
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.reply")))
    print("element 찾기 완료")
except:
    print("element 찾기 실패")

replies = driver.find_elements_by_css_selector('span.reply')

for reply in replies:
	reply.click()
	time.sleep(3)
	allhandles = driver.window_handles
	print(f'Total {allhandles} windows has been opened.')
	# 답글을 달 블로그 주소창으로 이동한다. 
	driver.switch_to.window(allhandles[1]) 
	time.sleep(2)
	print(f'current url => {driver.current_url}')
	# iframe 안으로 들어감
	driver.switch_to.frame('mainFrame')
	time.sleep(1)
	driver.find_element_by_css_selector('label.u_cbox_guide').click()
	time.sleep(1)
	# 랜덤 답글 생성 
	reply = reply_maker.make_reply_blog()
	pyperclip.copy(reply)
	action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
	time.sleep(1)
	driver.find_element_by_css_selector('.u_cbox_btn_upload').click()
	pyautogui.alert(text = '계속하시겠습니까?', title='title', button='예')
	driver.close()
	time.sleep(1)
	# 다시 원래 사이트로 돌아와야 됨.
	driver.switch_to.window(allhandles[0]) 
	