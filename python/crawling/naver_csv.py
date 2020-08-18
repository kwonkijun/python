import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

#https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC


search = input('검색어를 입력하세요 : ')
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.api_txt_lines.total_tit')
searchList = []

for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

f = open(f'{search}.csv', 'w', encoding='CP949', newline='') # Windows 경우 csv 모듈에서 데이터를 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제가 있는데 이를 newline 으로 해결한다. 
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()

print('완료 되었습니다.')