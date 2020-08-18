import urllib.request as req
from urllib.parse import urlencode

API = "https://api.ipify.org"

values = {
    'format' : 'json'
}

print('before', values)
params = urlencode(values) # url 형태로 데이터 표시형식을 변환시켜 준다
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)