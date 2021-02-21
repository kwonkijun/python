import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = 'https://www.coupang.com/np/search?q=%EA%B3%A0%EC%B6%94%EC%9E%A5&page=1'

response = requests.get(url, headers={'User-Agent' : 'Mozilla/5.0'})
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

items = soup.select("ul#productList > li")
result = []

for item in items:
    if len(item.select("span.ad-badge")) > 0:
        print("광고상품입니다.")
    else:
        print("일반상품입니다. sub_url수집")
        a = item.select_one("a.search-product-link")
        sub_url = "https://www.coupang.com/" + a.attrs['href']
        product_price = item.select_one("strong.price-value").text

        response = requests.get(sub_url, headers={'User-Agent' : 'Mozilla/5.0'})
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        brand_name = soup.select_one("a.prod-brand-name").text
        product_name = soup.select_one("h2.prod-buy-header__title").text
        print(brand_name, product_name, product_price, sub_url)
        result.append([brand_name, product_name, product_price, sub_url])

cur = datetime.now().strftime("%Y-%m-%d")
filename = f'쿠팡조회결과_{cur}.csv'
df = pd.DataFrame(result, columns=['brand_name', 'product_name', 'product_price', 'sub_url'])
df.to_csv(filename, index=False, encoding='euc-kr')