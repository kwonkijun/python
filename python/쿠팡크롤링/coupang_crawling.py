import requests
from bs4 import BeautifulSoup
import csv
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")
url = f'https://www.coupang.com/np/search?q={keyword}'

response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
html = response.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.select("ul#productList > li")

f = open(f"{keyword}_data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['번호', '브랜드명', '제품명', '가격', '상세페이지'])

for i, item in enumerate(items, 1):
    if len(item.select("span.ad-badge")) > 0:
        print("광고상품입니다.")
    else:
        a = item.select_one("a.search-product-link")
        sub_url = "https://www.coupang.com/" + a.attrs['href']
        product_price = item.select_one("strong.price-value").text

        response = requests.get(sub_url, headers={'User-Agent' : 'Mozilla/5.0'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        brand_name = soup.select_one("a.prod-brand-name").text
        product_name = soup.select_one("h2.prod-buy-header__title").text
        print(i, brand_name, product_name, product_price, sub_url)
        csvWriter.writerow([i, brand_name, product_name, product_price, sub_url])

f.close()