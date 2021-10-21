import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.palmyhillscc.co.kr/golfContents/visitList.asp"
browser = webdriver.Chrome('c:/chromedriver.exe')
browser.get(url)

# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# dates = soup.select("table.df_table td.txtCenter:nth-child(4)")
# dates.sort()
# print(dates)