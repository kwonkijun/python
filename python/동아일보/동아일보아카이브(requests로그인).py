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

# session 객체로 url을 접근 할 때는 get함수 사용. 
code = sess.get("https://www.donga.com/archive/newslibrary/view?idx=20041227%2F0002318342%2F1")

soup = BeautifulSoup(code.text, "html.parser")
print(soup)
content = soup.select_one("div.article_txt")
print(content.text)
