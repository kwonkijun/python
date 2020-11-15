from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

hashtag = input("좋아요 누를 해시태그 입력하세요:")

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

index = 1
posts = driver.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w > a")

while True:
	try:
		print("좋아요 작업중..")
		posts[index].click()
		time.sleep(3)
		driver.find_element_by_css_selector("span > .wpO6b").click()
		time.sleep(1)
		driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG > .wpO6b").click()
		index += 1
	except:
		print("1페이지 작업완료")
		driver.find_element_by_css_selector("body").send_keys(Keys.END)
		time.sleep(4)
		posts = driver.find_elements_by_css_selector(".v1Nh3.kIKUG._bz0w > a")
	