from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import csv

driver = webdriver.Chrome()
url = "https://publichealth.jmir.org/search/searchResult?field%5B%5D=text&criteria%5B%5D=healthcare+blockchain"
driver.implicitly_wait(3)
driver.get(url) 

try: 
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resultArea > article:nth-child(1)")))
    print("element 찾기 완료")
except:
    print("element 찾기 실패")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') 

pageNumber = soup.select('.pagination-wrapper > a')[-1].get_text() # 페이지 최종 찾기
pageNumber = 3 # 이 부분을 변경해 보세요!! 3 = 3페이지까지 크롤링
resultArea = soup.select_one('#resultArea') 

articles = []

sections = resultArea.select('.span9.articleInfo.details') 

for i, section in enumerate(sections, 1): 
	title = section.select_one('.articleTitle.title > a').get_text() 
	author = section.select('.authors > p')[0].get_text()
	company = section.select('.authors > p')[1].get_text()
	abstract = section.select_one('.TOC-abstract > p').get_text()
	articles.append([title, author, company, abstract])
	#print(f'{i} . title : {title} \n\n author : {author} \n\n company : {company} \n\nabstract : {abstract}\n\n')

for i in range(pageNumber-1):
	driver.find_element_by_css_selector('.nextPage').click()

	try: 
		element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#resultArea > article:nth-child(1)")))
		print("element 찾기 완료")
	except:
		print("element 찾기 실패")

	html = driver.page_source 
	soup = BeautifulSoup(html, 'html.parser') 

	resultArea = soup.select_one('#resultArea') 
	sections = resultArea.select('.span9.articleInfo.details') 

	for i, section in enumerate(sections, 1): 
		title = section.select_one('.articleTitle.title > a').get_text() 
		author = section.select('.authors > p')[0].get_text()
		company = section.select('.authors > p')[1].get_text()
		abstract = section.select_one('.TOC-abstract > p').get_text()
		articles.append([title, author, company, abstract])
		#print(f'{i} . title : {title} \n\n author : {author} \n\n company : {company} \n\nabstract : {abstract}\n\n')

# 엑셀 파일로 저장
f = open('결과.csv', 'w', encoding='utf-8-sig', newline='')  
tabs = ['title', 'author', 'company', 'abstract']
csvWriter = csv.writer(f)
csvWriter.writerow(tabs)
for i in articles:
    csvWriter.writerow(i)

f.close()