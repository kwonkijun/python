import requests # requests 라이브러리를 가져온다. 
from bs4 import BeautifulSoup # BeautifulSoup 라이브러리를 가져온다. 

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url) # request의 get함수를 이용해서 요청을 보낸다. (response 객체가 반환됨)

if(response.status_code == 200):
    html = response.text # response 객체 안에 html소스를 가져온다. 
    soup = BeautifulSoup(html, 'html.parser') # html 을 자르기 위한 파서 = html.parser
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
    print(title.get_text())
    # print(soup.prettify()) # HTML 코드를 이쁘게 보여준다. 
else:
    print(response.status_code)
