import requests
from bs4 import BeautifulSoup

keyword = input('검색어를 입력하세요 : ')

url = 'https://kin.naver.com/search/list.nhn'

params = {
    'query' : keyword
}

response = requests.get(url, params=params)

if(response.status_code == 200):
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.basic1')
    lis = ul.select('li')
    for li in lis:
        title = li.select_one('dl > dt > a').get_text()
        date = li.select_one('dl > dd.txt_inline').get_text()
        print(date, title)
    
else:
    print(response.status_code)