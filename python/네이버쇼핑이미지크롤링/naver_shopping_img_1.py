import requests
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://shopping.naver.com/department/home"

driver = webdriver.Chrome(r'C:\chromedriver')
driver.implicitly_wait(10)
driver.get(url)

imgs = driver.find_elements_by_css_selector('div._2WXH1ItBwq > img._1ODFOxs9pO._3p8l2pSAuq')

for idx, img in enumerate(imgs):
    img_url = img.get_attribute('src')
    response = requests.get(img_url)
    response.raise_for_status()
    
    with open(f"item{idx}.jpg", "wb") as f:
        f.write(response.content)

    