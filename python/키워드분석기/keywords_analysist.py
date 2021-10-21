import requests
import json
import pyautogui
import time
import csv

sub_list = ['ㄱ','ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
search_keyword = pyautogui.prompt("키워드를 입력하세요")
first_keywords = []

for sub in sub_list:
    main_keyword = search_keyword + ' ' + sub
    response = requests.get(f"https://ac.search.naver.com/nx/ac?q={main_keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")
    result = response.text.split("_jsonp_8(")[1][:-1]
    jsdata = json.loads(result)
    for data in jsdata['items'][0]:
        if len(data[0]) < 13 and data[0] not in first_keywords:
            print("[자동완성 검색어 추가 : 1차 키워드] - " + data[0])
            first_keywords.append(data[0])
        time.sleep(0.15)

print(f"[네이버 1차 키워드 {len(first_keywords)}개 추출 완료..!] {first_keywords} ")
print("[키워드별 검색량, 문서수 추출중]")

url = 'https://whereispost.com/keyword/functionmas.php'
header = {
    "User-Agent" : "Mozilla/5.0",
    "referer" : 'https://whereispost.com/keyword/'
}

f = open(f"./{search_keyword}.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(["키워드", "PC검색량", "모바일검색량", "총검색량", "문서수", "비율"])

for keyword in first_keywords:
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
    csvWriter.writerow([keyword, pc, mobile, total, posts, ratio])
    time.sleep(0.2)
f.close()
pyautogui.alert(text = f"분석이 완료 되었습니다!")
