import requests
from bs4 import BeautifulSoup
import pyautogui
import os
import openpyxl
import pandas

keyword = pyautogui.prompt(text="검색어를 입력하세요", title="Message")
start_date = pyautogui.prompt(text="시작날짜를 입력하세요\n(ex)2021.01.01", title="Message")
end_date = pyautogui.prompt(text="종료날짜를 입력하세요\n(ex)2021.01.01", title="Message")

cur_page = 1 # 현재 페이지

# 리스트 생성
news = [] # 뉴스
links = [] # 링크

pageCnt = 1
try:
    while True: # 반복문
        print(f'========현재 페이지 {cur_page}=========')
        url = f'https://search.naver.com/search.naver?&where=news&query={keyword}&start={pageCnt}&ds={start_date}&de={end_date}&pd=3'
        print(url)

        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        a_tags = soup.select("div.news_area > a")
        for a in a_tags:
            link = a.attrs['href']
            if link in links:
                raise ValueError
            title = a.get_text(strip=True)
            
            links.append(link)
            news.append([title, link])
        cur_page += 1
        pageCnt += 10
except ValueError:
    pass

print("크롤링 완료!! 엑셀에 저장합니다...")
df = pandas.DataFrame(news)
df.to_excel('result.xlsx', header=['제목', '링크'], index=None)
