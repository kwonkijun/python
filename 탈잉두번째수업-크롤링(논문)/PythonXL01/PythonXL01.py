import urllib.request
from bs4 import BeautifulSoup

import xlwings as xw

@xw.sub  # only required if you want to import it or run it via UDF Server
def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    
    url = 'https://comp.wisereport.co.kr/company/c1010001.aspx?cmp_cd=005930'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    price = soup.select_one('#cTB11 > tbody > tr:nth-child(1) > td > strong').get_text()
    strip_price = price.replace('\n', '').strip()
    print(strip_price)
    sheet.range('D6').value = strip_price


@xw.func
def hello(name):
    return "hello {0}".format(name)


if __name__ == "__main__":
    xw.Book("PythonXL01.xlsm").set_mock_caller()
    main()
