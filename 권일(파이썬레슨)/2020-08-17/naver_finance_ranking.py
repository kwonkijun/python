# 네이버 금융 사이트 
# 실시간 검색량 상위 종목 스크래핑 
# ---2020-08-17
# ---ver 1.0 

import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'

response = requests.get(url)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
for tr in trs:
    name = tr.select_one('th > a').get_text()
    price = tr.select_one('td').get_text()
    change_direction = tr['class'][0]
    change_price = tr.select_one('td > span').get_text()
    print(name, price, change_direction, change_price)
    


# 현재가, 뉴스(네이버금융에 있는..) 
    