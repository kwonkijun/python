import requests
from bs4 import BeautifulSoup
import time
import json
from urllib import parse
from html.parser import HTMLParser

# &lt &gt 등과 같은 문자는 HTMLParser로 변환이 안된다. 직접변환해주자. 
def myHTMLParser(string):
    result = string.replace("&lt", "<").replace("&gt", ">")
    return result

now_page = 1
prev_list = []

while True:

    response = requests.get(f"https://blog.naver.com/PostTitleListAsync.nhn?blogId=truelo&viewdate=&currentPage={now_page}&categoryNo=&parentCategoryNo=&countPerPage=10")  

    json_text = response.text.replace("\\", "\\\\")
    result = json.loads(json_text) # json 을 딕셔너리 자료형으로 변환시켜줍니다.

    # 이전 페이지 결과와 완전히 동일하다면 종료
    if result['postList'] == prev_list:
        break

    for idx, post in enumerate(result['postList'], (now_page - 1) * 10 + 1):
        # URL 형식으로 된 데이터를 urllib.parse 의 unquote_puls 로 변환시켜준다.
        title = parse.unquote_plus(post['title'].replace("+", " "), encoding="utf-8")
        # HTML ESCAPE 문자들은 그대로 남아있음, Beautifulsoup의 html.parser 를 이용해 준다. 
        title = myHTMLParser(BeautifulSoup(title, 'html.parser').text)
        print(f'{idx}.{title}')
            
    # 페이지의 포스트개수가 10개 이하이면 종료
    if len(result['postList']) < 10:
        break
    
    # 리스트 비교를 위한 저장
    prev_list = result['postList']
    now_page += 1
