# 네이버 금융 사이트 
# 실시간 검색량 상위 종목 스크래핑 
# ---2020-08-17
# ---ver 1.0 
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 엑셀객체 생성
write_wb = Workbook()

# 엑셀시트 생성
write_ws = write_wb.create_sheet('실시간검색상위종목')

url = 'https://finance.naver.com/'

response = requests.get(url)
response.raise_for_status()

html = response.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.select_one('#container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody')
trs = tbody.select('tr')
# 빈 리스트 생성 
stocks = []
for tr in trs:
    name = tr.select_one('th > a').get_text()
    price = tr.select_one('td').get_text()
    change_direction = tr['class'][0]
    change_price = tr.select_one('td > span').get_text()
    # 변수들을 리스트에 저장 
    temp_list = [name, price, change_direction, change_price]
    stocks.append(temp_list)

# 행단위로 입력
for stock in stocks:
    write_ws.append(stock)

write_wb.save(r'C:\Users\kwonkijun\Desktop\프로젝트(최신)\파이썬\권일(파이썬레슨)\2020-08-20\실시간종목.xlsx')
