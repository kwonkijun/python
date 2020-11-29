from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import pyautogui
import csv


keyword = pyautogui.prompt(text='검색어를 입력하세요', title='Message', default='입력하세요')
lastPage = pyautogui.prompt(text='몇 페이지까지 검색할까요?', title='Message', default='입력하세요')

page = 1
searchList = []

for i in range(1,int(lastPage)+1):
    baseUrl = 'https://kin.naver.com/search/list.nhn?query='
    url = baseUrl + parse.quote_plus(keyword) + '&page=' + str(i)

    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.select('#s_content > div.section > ul > li')

    print(f"------------------------------{i}번째 페이지----------------------------")
    for idx, li in enumerate(lists, 1):
        title = li.select_one('dl > dt > a').get_text()
        date = li.select_one('dl > dd.txt_inline').get_text()
        content = li.select_one('dl > dd:nth-child(3)').get_text()
        print(f'{date}\n{title}\n{content}')

