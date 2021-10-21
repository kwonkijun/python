from json import decoder
import requests
import json
url = 'https://whereispost.com/keyword/functionmas.php'
keywords = [
    '파워포인트 배경',
    '파워포인트 뷰어',
    '파워포인트 배경제거',
    '파워포인트 바이블',
    '파워포인트 베스트 팁',
    '파워포인트 보고서',
    '파워포인트 보고서 디자인 기술',
    '파워포인트 블루스',
    '파워포인트 블루스+slide',
    '파워포인트 비밀노트 533',
    '파워포인트 세로',
    '파워포인트 설치',
    '파워포인트 사이즈',
    '파워포인트 시험',
    '파워포인트 슬라이드 크기',
    '파워포인트 사진'
]
header = {
    "User-Agent" : "Mozilla/5.0",
    "referer" : 'https://whereispost.com/keyword/'
}

for keyword in keywords:
    data = {
        "query" : keyword,
        "s" : 'true'
    }

    response = requests.post(url, data, headers=header)
    response.encoding = 'utf-8-sig'
    res_data = json.loads(response.text)
    
    pc = int(res_data['pc'].replace(',', '')) # PC 검색량
    mobile = int(res_data['mo'].replace(',', '')) # Mobile 검색량
    total = pc + mobile # 총 검색량
    posts = int(res_data['post'].replace(',','')) # 문서수
    try:
        ratio = posts / total # 문서수 / 총 검색량
    except ZeroDivisionError:
        ratio = 100
    # 총 검색량 (PC + mobile) 이 1000이 넘고, 
    # 문서수 / 총 검색량 비율이 1 이하인 키워드만 추출
    print(f"[키워드 : {keyword}] [PC : {pc}] [Mobile : {mobile}] [Total : {total}] [Posts : {posts}] [Ratio : {ratio}]")
    if total >= 1000 and ratio <= 1:
        print("찾았다!!", keyword)
