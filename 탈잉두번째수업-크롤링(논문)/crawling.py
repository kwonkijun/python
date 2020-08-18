import urllib.request
from bs4 import BeautifulSoup

url = 'https://publichealth.jmir.org/search/searchResult?field%5B%5D=text&criteria%5B%5D=healthcare+blockchain'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

resultArea = soup.select_one('#resultArea')
# articles = resultArea.select('.row.tocArticle.toc-article-card')

print(resultArea.html)