from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요 : ")

url = f'https://www.google.com/search?q={parse.quote_plus(keyword)}&sxsrf=ALeKk00_wjIF7OJq6cBi_PHtaJObHnvlzA:1586142552919&source=lnms&tbm=isch&sa=X&ved=2ahUKEwio6re76dLoAhUkw4sBHbqyCuUQ_AUoAXoECBgQAw&biw=1249&bih=833'

req = request.Request(url, headers={'User-Agent' : 'Mozilla/5.0'}) # 403 에러 시 헤더를 추가하면 접근 가능해 진다. (그냥 urlopen시 봇취급해서 접근을 막음)

html = request.urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

imgs = soup.select('a > img')
print(imgs)

for idx, img in enumerate(imgs):
    imgUrl = img.attrs['src']
    f = request.urlopen(imgUrl).read()
    with open(f'imgs/{keyword}{idx}.jpg', 'wb') as p:
        p.write(f)

# for idx , img in enumerate(imgs, 1):
#     imgUrl = img.attrs['data-source']
#     f = request.urlopen(imgUrl).read()
#     with open(f'imgs/{keyword}{idx}.jpg', 'wb') as p:
#         p.write(f)

