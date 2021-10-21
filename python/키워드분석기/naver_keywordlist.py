import requests
import json
import pyautogui
import os

sub_list = ['ㄱ','ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
keyword = pyautogui.prompt("키워드를 입력하세요")
f = open(f"{keyword}.txt", 'w', encoding='utf-8')

for sub in sub_list:
    main_keyword = keyword + ' ' + sub
    print(main_keyword)
    response = requests.get(f"https://ac.search.naver.com/nx/ac?q={main_keyword}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_8")
    result = response.text.split("_jsonp_8(")[1][:-1]
    jsdata = json.loads(result)
    for data in jsdata['items'][0]:
        f.write(data[0] + '\n')

f.close()
pyautogui.alert(text = f"연관검색어 추출이 완료 되었습니다!\n")