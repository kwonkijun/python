# requests 라이브러리
# BeautifulSoup 라이브러리
import requests as req
from bs4 import BeautifulSoup

page_num = 1
# 2 페이지 까지 크롤링
total_news_content = ""

while page_num < 31:
	url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%ED%95%9C%EA%B5%AD%EA%B1%B0%EB%9E%98%EC%86%8C&start={page_num}"	
	# 사이트에 접속해서 html 데이터 가져오기
	response = req.get(url, headers={"User-Agent" : "Mozilla/5.0"})

	# status.code = 200 접속 성공
	# print(response.status_code)

	# html 가공하기
	html = response.text
	soup = BeautifulSoup(html, "html.parser")

	headers = soup.select("div.info_group")
	print(f"{page_num}번째 페이지 크롤링 중입니다..")

	for header in headers:
		link = header.select("a.info")
		# 네이버뉴스 링크가 있는 기사들만 크롤링
		if(len(link) > 1):
			news_url = link[1].attrs['href']
			response = req.get(news_url, headers={"User-Agent" : "Mozilla/5.0"})
			news_html = response.text
			news_soup = BeautifulSoup(news_html, "html.parser")
			
			news_title = news_soup.select_one("#articleTitle").string
			news_content = news_soup.select_one("#articleBodyContents").text

			if "// flash 오류를 우회하기 위한 함수 추가" in news_content:
				news_content = news_content.replace("// flash 오류를 우회하기 위한 함수 추가", "")
				news_content = news_content.replace("function _flash_removeCallback() {}", "")

			news_content = news_content.strip() # 양쪽 공백 제거
			total_news_content += news_content
			print(f"뉴스제목\n{news_title}\n본문내용\n{news_content}")

	page_num += 10


print("뉴스 데이터 크롤링 완료!")

# konlpy 모듈을 사용하기 위해서는 
# 1. JDK 설치 (환경변수 설정)
# 2. jpype1 모듈 설치 pip install jpype1
# 3. konlpy 모듈 설치 pip install konlpy

# 데이터분석
print("데이터 분석을 시작합니다.")
print("명사 추출 중입니다..")
from konlpy.tag import Okt
okt = Okt()
nouns = okt.nouns(total_news_content)

# 빈도수 측정
from collections import Counter
count = Counter(nouns)

# 한글자인 녀석들 골라내기
temp = count.copy()
for i in temp.keys():
	if(len(i)==1):
		del count[i]

print(count)
