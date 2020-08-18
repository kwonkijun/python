import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요: '))
pageNum = 1
count = 1
i = input('몇 페이지 크롤링 할까요? : ')
lastPage = int(i) * 10 - 9

while pageNum <= lastPage :
    
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all(class_='sh_blog_title') 

    print(f'--------{count}페이지 결과 입니다---------')
    for i in title:
        print(i.attrs['title']) 
        print(i.attrs['href']) 
        print()
    print()
    pageNum += 10
    count += 1



#https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=tab_pge&srchby=all&st=sim&where=post&start=11