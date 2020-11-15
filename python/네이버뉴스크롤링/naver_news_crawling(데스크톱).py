import requests as req
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%95%9C%EA%B5%AD%EA%B1%B0%EB%9E%98%EC%86%8C"

response = req.get(url, headers={'User-Agent': 'Mozilla/5.0'})
print(response.status_code)

html = response.text
soup = BeautifulSoup(html, "html.parser")
headers = soup.select("div.info_group")

total_news_content = ""
for header in headers:
	link = header.select("a.info")
	if(len(link) > 1):
		news_url = link[1].attrs['href']
		response = req.get(news_url, headers={'User-Agent': 'Mozilla/5.0'})
		news_html = response.text
		news_soup = BeautifulSoup(news_html, "html.parser")
		news_title = news_soup.select_one("#articleTitle").string
		news_content = news_soup.select_one("#articleBodyContents").text
		
		if "// flash 오류를 우회하기 위한 함수 추가" in news_content:
			news_content = news_content.replace("// flash 오류를 우회하기 위한 함수 추가", "")
			news_content = news_content.replace("function _flash_removeCallback() {}", "")

		news_content = news_content.strip() 
		total_news_content += news_content
		print(f"뉴스제목 \n {news_title}\n본문내용\n{news_content}")

print("뉴스 데이터 크롤링 완료!")

# 형태소 분석 시작
print("형태소 분석을 시작합니다.")
from konlpy.tag import Okt
okt = Okt()
print("명사만 추출합니다..")
nouns = okt.nouns(total_news_content)

# 명사 빈도수 카운트
from collections import Counter
count = Counter(nouns)

# 불용어 제거 ('는' '그' '가' 등)
temp = count.copy()
for i in temp.keys(): 
	if len(i) == 1:
		del count[i]

print(count)

# 이미지 가져오기
import numpy as np
from PIL import Image
image_list = np.array(Image.open(r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\네이버뉴스크롤링\img.PNG"))

# 이미지 색 뽑아오기
from wordcloud import ImageColorGenerator
image_color = ImageColorGenerator(image_list)

# 단어구름 만들기
from wordcloud import WordCloud
wordcloud = WordCloud(font_path=r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\네이버뉴스크롤링\NanumBarunGothic.ttf", background_color="white", mask=image_list).generate_from_frequencies(count)

# 단어구름 띄우기
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.imshow(wordcloud.recolor(color_func=image_color), interpolation="bilinear")
plt.axis('off')
plt.show()