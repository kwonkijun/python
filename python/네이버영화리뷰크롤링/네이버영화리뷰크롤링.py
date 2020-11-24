from bs4 import BeautifulSoup
import requests

page_num = 1
review_count = 0

url = f'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=190722&target=after&page={page_num}'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")
max_count = int(soup.select_one(".c_88.fs_11").string)

while True:
	comments = soup.select("td.title")

	if(len(comments) == 0):
		break

	for comment in comments:
		review_count += 1
		text = comment.select_one("br").next_sibling.strip()
		print(f'{review_count}. {text}')
		
	if(review_count == max_count):
		break

	page_num += 1
	url = f'https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=190722&target=after&page={page_num}'
	res = requests.get(url)
	html = res.text
	soup = BeautifulSoup(html, "html.parser")