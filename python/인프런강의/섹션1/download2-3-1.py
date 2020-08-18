import urllib.request as req
from urllib.parse import urlparse
url = "http://www.encar.com"

mem = req.urlopen(url)

print(mem)

print("geturl", mem.geturl()) # 현재 url 출력 
print("status", mem.status) # 상태코드 200 , 404, 403, 500
print("headers", mem.getheaders()) # 헤더 출력
print("info", mem.info()) # 헤더부분을 이쁘게 출력 
print("code", mem.getcode()) # 상태코드
print("read", mem.read(10)) # 변수로 숫자를 넣으면 해당 바이트 만큼 가져온다. 
print("decode", mem.read(50).decode("utf-8"))

print(urlparse("http://www.encar.com?test=test"))