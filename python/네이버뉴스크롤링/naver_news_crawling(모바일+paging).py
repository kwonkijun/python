import requests
from bs4 import BeautifulSoup
import urllib.parse as parse

keyword = input("검색어를 입력하세요: ")
keyword = parse.quote(keyword)

article_num = 1
while True:
	# 네이버뉴스 URL주소
	url = f"https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={keyword}&start={article_num}"
	# https://m.search.naver.com/search.naver?where=m_news&sm=mtb_pge&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&start=1
	# request 모듈을 사용하면 크롤링이 멈추지 않는다
	html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
	soup = BeautifulSoup(html, "html.parser")

	# 1페이지 뉴스기사
	articles = soup.select("div.news_wrap")

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
	
	if(len(articles) != 15):
		break
	
	article_num += article_num + 15
