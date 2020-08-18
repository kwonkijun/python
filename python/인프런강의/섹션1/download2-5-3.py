from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
            <li><a href="http://www.google.com">google</a></li>
            <li><a href="http://www.tistory.com">tistory</a></li>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all('a')
a = soup.find_all("a", string="daum")
b = soup.find_all("a", limit=3) # 가져오는 숫자에 제한을 건다.

for a in links:
    href = a.attrs['href']
    txt = a.string