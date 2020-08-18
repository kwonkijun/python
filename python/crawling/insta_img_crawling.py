from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time 

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색어를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl) 

# 인스타그램의 경우 대부분 자바스크립트로 페이지가 만들어져서 BeautifulSoup 만으로는 크롤링이 안된다. -> selenium 사용. 

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

insta = soup.select('.v1Nh3.kIKUG._bz0w') #select 와 find 차이 select에서는 css selector 를 사용할 수 잇다 기능적으로는 동일하다. 

n = 1
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/'+ plusUrl + str(n)  + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)

print('저장이 완료됬습니다. ')
driver.close()