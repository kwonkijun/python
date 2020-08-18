from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import os
import errno

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = parse.quote_plus("사자")
url = base + quote

html = request.urlopen(url)
savePath = "C:\\imagedown\\"

# 폴더 만들기 
try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST: 
        print("폴더 만들기 실패!")

soup = BeautifulSoup(html, 'html.parser')
img_list = soup.select('div.img_area > a.thumb._thumb > img')

# 랜더링 되기전 속성값을 항상 확인해야 한다. (img src에 있는게 아니라 data-source값에 있음)

for i, img_list in enumerate(img_list, 1):
    fullFileName = os.path.join(savePath, savePath + str(i)  + '.jpg')
    request.urlretrieve(img_list['data-source'], fullFileName) # 이미지 다운로드 -> urlretrieve 활용

