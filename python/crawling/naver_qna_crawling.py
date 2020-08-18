from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import csv

# 기본적으로 2가지 모듈이 필요하다. 

# https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC

keyword = input('검색어를 입력하세요')
lastPage = input('몇 페이지까지 검색?')
page = 1
searchList = []

for i in range(1,int(lastPage)+1):
    baseUrl = 'https://kin.naver.com/search/list.nhn?query='
    url = baseUrl + parse.quote_plus(keyword) + '&page=' + str(i)

    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.select('#s_content > div.section > ul > li')

    print(f"------------------------------{i}번째 페이지----------------------------")
    for idx, li in enumerate(lists, 1):
        temp = []
        title = li.select_one('dl > dt > a').get_text()
        date = li.select_one('dl > dd.txt_inline').get_text()
        content = li.select_one('dl > dd:nth-child(3)').get_text()
        temp.append(title)
        temp.append(date)
        temp.append(content)
        searchList.append(temp)

f = open(f'{keyword}.csv', 'w', newline='', encoding='euc-kr')
writer = csv.writer(f)
for i in searchList:
    writer.writerow(i)

f.close()
# enumerate '열거하다' 순서가 잇는 자료형(tuple, list, string)을 첫번째 인자로 받아서 각각의 index 값과 value 값들을 enumerate 객체로 리턴한다. 


