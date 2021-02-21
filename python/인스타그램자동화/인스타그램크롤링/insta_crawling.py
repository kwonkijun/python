from selenium import webdriver
import pyautogui
import time
import random
import json
from datetime import datetime

hashtag = pyautogui.prompt(text='해시태그를 입력하세요', title='Message', default='입력하세요')

# 상수
DRIVER_URL = r"C:\chromedriver.exe"
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

driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(3)

driver.get(TAG_URL)
time.sleep(5)

insta_dic = driver.execute_script("return window._sharedData")

top_posts = insta_dic['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']

for post in top_posts:
	likes = post['node']['edge_liked_by']['count']
	comments = post['node']['edge_media_to_comment']['count']
	timestamp = post['node']['taken_at_timestamp']
	print(likes, comments, datetime.fromtimestamp(timestamp))

# first_post = driver.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w > a")
# first_post.click()

# 사진
# imgs = driver.find_elements_by_css_selector("div.eLAPa.RzuR0 > div.KL4Bh > img.FFVAD")

# for img in imgs:
# 	img_url = img.get_attribute('src')
# 	print(img_url)

# # 좋아요 개수
# like_count = driver.find_element_by_css_selector("a.zV_Nj > span").text

# while True:
	
# 	time.sleep(2)
# 	# 좋아요버튼
# 	driver.find_element_by_css_selector("span.fr66n > button.wpO6b").click()
# 	time.sleep(random.randint(1,3))

# 	try:
# 		driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow").click()
# 	except:
# 		print("마지막 포스팅입니다...")
# 		print("작업완료")
# 		break

	