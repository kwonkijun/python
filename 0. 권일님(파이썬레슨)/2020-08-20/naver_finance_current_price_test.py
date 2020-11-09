import requests
from bs4 import BeautifulSoup

codes = ['010130', '012620', '098460', '084990']

for code in codes:
    url = 'https://finance.naver.com/item/main.nhn?code=' + code 

    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    today = soup.select_one('#chart_area > div.rate_info > div')
    price = today.select_one('.blind')
    print(price)