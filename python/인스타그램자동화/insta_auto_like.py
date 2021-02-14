from selenium import webdriver
import pyautogui
import time
import random
import pyperclip
import reply_maker
from selenium.webdriver.common.keys import Keys

hashtag = pyautogui.prompt(text='해시태그를 입력하세요', title='Message', default='입력하세요')

# 상수
DRIVER_URL = r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\selenium\chromedriver.exe"
LOGIN_URL = "https://www.instagram.com/accounts/login/?hl=ko"
USER_ID = "startcoding73"
USER_PW = "1q2w3e4r!@@"
TAG_URL = f"https://www.instagram.com/explore/tags/{hashtag}/?hl=ko"

driver = webdriver.Chrome(DRIVER_URL)
driver.get(LOGIN_URL)
driver.implicitly_wait(3)

driver.find_element_by_name("username").send_keys(USER_ID)
time.sleep(1)

driver.find_element_by_name("password").send_keys(USER_PW)
time.sleep(1)

driver.find_element_by_css_selector(".Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(3)

driver.get(TAG_URL)
time.sleep(5)

first_post = driver.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w > a")
print("좋아요 + 댓글 작업중..")
first_post.click()
while True:
	try:
		time.sleep(random.randint(5,10))
		# 좋아요버튼
		driver.find_element_by_css_selector("span > .wpO6b").click()
		time.sleep(random.randint(1,3))
		# 댓글버튼
		driver.find_element_by_css_selector(".X7cDz").click()
		time.sleep(random.randint(1,2))
		
		pyperclip.copy(reply_maker.make_reply_insta())
		time.sleep(random.randint(1,2))
		pyautogui.hotkey("ctrl", "v")

		driver.find_element_by_css_selector("form > .sqdOP.yWX7d.y3zKF").click()
		time.sleep(random.randint(1,2))
		try:
			driver.find_element_by_css_selector("._65Bje.coreSpriteRightPaginationArrow").click()
		except:
			print("마지막 포스팅입니다...")
			print("작업완료")
			break
	except:
		print("댓글 입력 오류")
		driver.find_element_by_css_selector("._65Bje.coreSpriteRightPaginationArrow").click()
	
	