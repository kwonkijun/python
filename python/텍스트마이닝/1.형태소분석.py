import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요: ")
keyword = parse.quote(keyword)
# 네이버뉴스 URL주소
url = f"https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={keyword}"

# request 모듈을 사용하면 크롤링이 멈추지 않는다
html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
soup = BeautifulSoup(html, "html.parser")

# 1페이지 뉴스기사
articles = soup.select("div.news_wrap")

# 전체 본문 데이터 
total_news_content = ""

for article in articles:
	haslink = article.select("span.info")
	# 뉴스기사 중 네이버뉴스가 아닌 것은 크롤링에서 제외
	if(len(haslink) == 1):
		continue
	title = article.select_one("a.news_tit")
	news_url = title.attrs["href"]

	# 실제 기사가 있는 페이지 소스를 가져온다
	news_html = requests.get(news_url, headers={'User-Agent': 'Mozilla/5.0'}).text
	news_soup = BeautifulSoup(news_html, "html.parser")
	news_title = news_soup.select_one("h2.media_end_head_headline").string
	news_date = news_soup.select_one("span.media_end_head_info_datestamp_time._ARTICLE_DATE_TIME").string
	news_content = news_soup.select_one("#newsct_article").get_text()
	
	print(f'뉴스제목 : {news_title} \n날짜 : {news_date} \n기사 내용: {news_content}')
	total_news_content += news_content

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
image_list = np.array(Image.open(r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\텍스트마이닝\img.PNG"))

# 이미지 색 뽑아오기
from wordcloud import ImageColorGenerator
image_color = ImageColorGenerator(image_list)

# 단어구름 만들기
from wordcloud import WordCloud
wordcloud = WordCloud(font_path=r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\텍스트마이닝\NanumBarunGothic.ttf", background_color="white", mask=image_list).generate_from_frequencies(count)

# 단어구름 띄우기
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.imshow(wordcloud.recolor(color_func=image_color), interpolation="bilinear")
plt.axis('off')
plt.show()