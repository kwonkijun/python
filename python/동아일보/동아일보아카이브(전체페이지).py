from bs4 import BeautifulSoup
import requests

# 로그인이 필요한 페이지의 경우, requests 모듈을 활용해서도 가능하다


sess = requests.session()
# Referer : 내가 어디에서 왔는지 알려주는 것. 
header = {"Referer": "https://secure.donga.com/membership/login.php?gourl=http%3A%2F%2Fwww.donga.com%2F%3F"}
# Network 탭 -> preserved log 체크, post 형식의 요청을 확인한다
# 가장아래에 form data 부분을 복사해준다. 
post_data = {
    "gourl": "https%3A%2F%2Fwww.donga.com%2F",
    "bid": "talingpython",
    "bpw": "xkfdldvkdlTjs2"
}
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=header, data=post_data)

# 뉴스기사제목 요소들 가져오기
code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=20041228")
soup = BeautifulSoup(code.text, "html.parser")
a = soup.select("ul.news_list a")
for i in a:
    article_num = i.attrs["onclick"].replace("javascript:getNewsArticle('20041228/", "").replace("/1'); return false;", "")

# session 객체로 url을 접근 할 때는 get함수 사용. 
    url = f"https://www.donga.com/archive/newslibrary/view?idx=20041228%2F{article_num}%2F1"
    code = sess.get(url)
    soup = BeautifulSoup(code.text, "html.parser")
    content = soup.select_one("div.article_txt")
    print(content.text)
