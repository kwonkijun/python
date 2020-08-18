import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + urllib.parse.quote_plus(plusUrl) #한국어를 주소값에 맞게 변환
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title') #find 는 조건에 맞는 한개를 찾고 find_all은 조건에 맞는 모든 태그를 찾는다. class는 예약어이기 때문에 마지막에 _를 붙여준다. 

for i in title:
    print(i.attrs['title']) #속성이 title 인 놈들만 출력 
    print(i.attrs['href']) #속성이 href 인 놈들만 출력
    print()