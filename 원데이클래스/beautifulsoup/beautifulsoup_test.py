import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('.basic1')
    my_lists = ul.select('li')
    for my_list in my_lists:
        title = my_list.select_one('dl > dt > a').get_text()
        print(title)

else : 
    print(response.status_code)


    
