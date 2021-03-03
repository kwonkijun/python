# 2021.02.23
# by startcoding
# 인스타그램 크롤러 (멘토링 프로그램)

from selenium import webdriver
import pyautogui
import time
from datetime import datetime

hashtag = pyautogui.prompt(text='해시태그를 입력하세요', title='Message', default='입력하세요')

# 상수
DRIVER_URL = r"C:\chromedriver.exe"
LOGIN_URL = "https://www.instagram.com/accounts/login/?hl=ko"
USER_ID = "startcoding73" # 아이디
USER_PW = "1q2w3e4r!@@" # 비밀번호
TAG_URL = f"https://www.instagram.com/explore/tags/{hashtag}/?hl=ko"

driver = webdriver.Chrome(DRIVER_URL)
driver.get(LOGIN_URL)
driver.implicitly_wait(3)

# 아이디 입력
driver.find_element_by_name("username").send_keys(USER_ID)
time.sleep(1)

# 비밀번호 입력
driver.find_element_by_name("password").send_keys(USER_PW)
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(3)

# 검색한 URL로 이동 
driver.get(TAG_URL)
time.sleep(5)

# 인스타그램 댓글 개수를 크롤링하는 게 selenium으로도 어렵습니다. (마우스를 올려놔야만 html 태그가 보여요!)

# window._sharedData 안에 많은 정보들이 담겨 있어요. 저는 이 데이터를 이용할 겁니다. 
insta_dic = driver.execute_script("return window._sharedData")

# 인기 게시물 정보는 아래와 같은 데이터경로에 있습니다. 
top_posts = insta_dic['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']

# 좋아요개수, 댓글개수, 날짜 수집 
for post in top_posts:
	likes = post['node']['edge_liked_by']['count']
	comments = post['node']['edge_media_to_comment']['count']
	timestamp = post['node']['taken_at_timestamp']
	print(likes, comments, datetime.fromtimestamp(timestamp))