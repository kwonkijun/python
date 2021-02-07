import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

SCROLL_PAUSE_TIME = 0.5
SCROLL_SCRIPT = 'return document.body.scrollHeight'

url = "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9A%B0%ED%84%B0"

driver = webdriver.Chrome(r'C:\chromedriver')
driver.implicitly_wait(10)
driver.get(url)

last_height = driver.execute_script(SCROLL_SCRIPT)

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내린다.
    driver.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script(SCROLL_SCRIPT)
    
    print(f'{last_height} {new_height}')
    if new_height == last_height:
        break
    last_height = new_height

# 이미지 크롤링
imgs = driver.find_elements_by_css_selector("a.thumbnail_thumb__3Agq6 > img")
for idx, img in enumerate(imgs):
    img_url = img.get_attribute('src')
    
    response = requests.get(img_url)
    response.raise_for_status()
    
    path = r'C:\Users\스타트코딩\Desktop\main\python\python\네이버쇼핑이미지크롤링\result'

    with open(f'{path}\item{idx}.jpg', 'wb') as f:
        f.write(response.content)
    