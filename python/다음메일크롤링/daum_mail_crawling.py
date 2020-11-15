from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Administrator\Desktop\기준\코딩교육\자료정리\파이썬\python\selenium\chromedriver.exe")

url = "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F" 
driver.get(url)

# id 입력
id = driver.find_element_by_css_selector("#id")
id.send_keys("kkj63691126")
# pw 입력
pw = driver.find_element_by_css_selector("#inputPwd")
pw.send_keys("koC3848!!@")
# 로그인 버튼 클릭
login_btn = driver.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
# 이메일 함으로 이동
driver.get("https://mail.daum.net") 
time.sleep(3)
# 이메일 제목 크롤링
# driver.find_element_by_css_selector() # select_one() 과 기능이 완전이 같다
title = driver.find_elements_by_css_selector("strong.tit_subject")
for i in title:
	print(i.text)

driver.close()