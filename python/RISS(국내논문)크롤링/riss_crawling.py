import requests
from bs4 import BeautifulSoup
import pyautogui
from selenium import webdriver
import time

keyword = pyautogui.prompt(title="논문검색", text="검색어를 입력하세요:")

url = f"http://riss.kr/search/Search.do?&pageNumber=1&query={keyword}&colName=re_a_kor&pageScale=10&iStartCount=0"

driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get(url)
time.sleep(4)

links = driver.find_elements_by_css_selector("div.srchResultListW p.title > a")

sub_urls = []
for link in links:
    sub_urls.append(link.get_attribute('href'))

for sub_url in sub_urls:
    driver.get(sub_url)
    time.sleep(4)

    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # title = soup.select_one("div.thesisInfoTop > h3.title").get_text(strip=True)
    # add_info = soup.select_one("div.text.off").get_text(strup=True)

    add_info = driver.find_element_by_css_selector("div.innerCont").text