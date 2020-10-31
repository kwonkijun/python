# 주의 사항 
# 동일한 게시글에 공감/공감취소를 6회 이상 반복 시 더 이상 해당 게시글에 공감을 누를 수 없습니다. 
# 위 기준을 3회 반복할 경우, 비정상적인 이용자로 판단하여 7일간 공감 기능이 제한됩니다. (네이버)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from my_modules import reply_maker
import pyperclip, pyautogui
import time
import telepot

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

# 블로그 홈으로 이동

page_num = 3 # 페이지 번호 
max_page_num = 7 # 마지막 페이지 번호
url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
driver.get(url)

# 좋아요 아이콘이 생기기 까지 기다리는 코드 
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".u_ico._icon")))
    print("element 찾기 완료")
except:
    print("element 찾기 실패")

# 좋아요 댓글 작업 
user_name_list = []
breaker = False
while True:
	# 현재 페이지 이웃 새글 가져오기 
	new_blogs = driver.find_elements_by_css_selector('div.item.multi_pic') 
	# 이웃 새글 마다 작업 
	for new_blog in new_blogs:
		# 좋아요 버튼이 눌렸으면 STOP 
		like_btn = new_blog.find_element_by_css_selector(".u_likeit_list_btn")
		print(like_btn.text)
		print(like_btn.get_attribute('aria-pressed')) 
		print(type(like_btn.get_attribute('aria-pressed')))
		while True:
			if(like_btn.get_attribute('aria-pressed') == None):
				time.sleep(2)
			else:
				break
		if(like_btn.get_attribute('aria-pressed') == 'false'):
			# 좋아요 버튼 클릭
			like_btn.click()
			time.sleep(3)
			# 이미 작업한 아이디면 댓글 PASS
			user_name = new_blog.find_element_by_css_selector(".name_author").text
			print(user_name)
			if(user_name not in user_name_list):
				user_name_list.append(user_name)
				# 댓글 버튼 클릭
				new_blog.find_element_by_css_selector("span.reply").click()
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
				# 댓글 버튼이 안눌렸으면 눌러준다 
				reply_btn = driver.find_element_by_css_selector('.area_comment')
				class_names = reply_btn.get_attribute('class')
				print(class_names)
				marker = class_names.split(' ')[1]
				print(marker)
				print(type(marker))
				if(marker == 'pcol2'):
					reply_btn.click()
					time.sleep(3)

				driver.find_element_by_css_selector('label.u_cbox_guide').click()
				time.sleep(1)
				# 랜덤 답글 생성 
				reply = reply_maker.make_reply_blog()
				reply_addName = f'{user_name}님 {reply}'
				pyperclip.copy(reply_addName)
				action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
				time.sleep(1)
				driver.find_element_by_css_selector('.u_cbox_btn_upload').click()
				time.sleep(1)
				driver.close()
				time.sleep(1)
				# 다시 원래 사이트로 돌아와야 됨.
				driver.switch_to.window(allhandles[0])
		else:
			print("좋아요 버튼이 눌렸음.")
			breaker = True
			break
	if(breaker == True): 
		break
	page_num += 1
	if(page_num > max_page_num):
		break
	url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
	driver.get(url)

	# off_btns = driver.find_elements_by_css_selector(".u_likeit_list_btn._button.off")
	# replies = driver.find_elements_by_css_selector('span.reply')
	# if(len(off_btns) > 0 and page_num <= max_page_num):
	# 	# 좋아요 버튼 클릭
	# 	for off_btn in off_btns:
	# 		off_btn.click()
	# 		time.sleep(2)
	# 	for reply in replies:
	# 		reply.click()
	# 		time.sleep(3)
	# 		allhandles = driver.window_handles
	# 		print(f'Total {allhandles} windows has been opened.')
	# 		# 답글을 달 블로그 주소창으로 이동한다. 
	# 		driver.switch_to.window(allhandles[1]) 
	# 		time.sleep(2)
	# 		print(f'current url => {driver.current_url}')
	# 		# iframe 안으로 들어감
	# 		driver.switch_to.frame('mainFrame')
	# 		time.sleep(1)
	# 		driver.find_element_by_css_selector('label.u_cbox_guide').click()
	# 		time.sleep(1)
	# 		# 이미 답글을 달은 적이 있는지 검사해야함
	# 		# 랜덤 답글 생성 
	# 		reply = reply_maker.make_reply_blog()
	# 		pyperclip.copy(reply)
	# 		action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
	# 		time.sleep(1)
	# 		driver.find_element_by_css_selector('.u_cbox_btn_upload').click()
	# 		time.sleep(1)
	# 		driver.close()
	# 		time.sleep(1)
	# 		# 다시 원래 사이트로 돌아와야 됨.
	# 		driver.switch_to.window(allhandles[0])
	# 	page_num += 1
	# 	url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
	# 	driver.get(url)
	# else:
	# 	break

# token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
# mc = '1021336969'
# bot = telepot.Bot(token)

# bot.sendMessage(mc, "블로그 이웃 새글 좋아요 댓글작업이 완료되었습니다.")