import os
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


try:
    if not(os.path.isdir('img')):
        os.mkdir('img')
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory")
        raise

baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusUrl = input('검색어를 입력하세요.')
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_img')

# 실제코드와 구글개발자도구의 코드가 다른 경우가 종종 있다. 
# 그 이유는 구글개발자도구의 코드는 자바스크립트를 거쳐서 나온 코드이기 때문. 
n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f: #파일을 열고 나서 닫을 필요가 없기 때문에 편리하다 
        with open(os.path.join(os.path.abspath('img') , plusUrl + str(n) + '.jpg'), 'wb') as h:
            img = f.read()
            h.write(img)
    n+= 1
    print(imgUrl)

print('다운로드 완료')