from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyperclip
import time

driver = webdriver.Chrome()
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.implicitly_wait(10) # get을 호출하기 전에 wait 시간을 10초로 설정하면 페이지가 모두 로딩될 때까지 기다린 후 다음 코드을 실행. 만약 2초에 로딩이 완료 됬다면 더 기다리지 않고 다음 코드를 실행. 
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

id ="kkj6369"
pw ="koC3848!!@"

receive_user = "kkj6369@naver.com"
mail_subject = "자동메일 테스트입니다.(제목)"
mail_content = "자동메일 테스트입니다.(내용)"

time.sleep(2)

# 아이디 클립보드에서 COPY 후 입력
pyperclip.copy(id)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.TAB).perform()
time.sleep(2)
# 패스워드 클립보드에서 COPY 후 입력 
pyperclip.copy(pw)
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys(Keys.ENTER).perform()
time.sleep(2)

# 자동 로그인 등록하지 않음 버튼 클릭
driver.find_element_by_xpath('//*[@id="new.dontsave"]').click()
time.sleep(2)
# 메일 버튼 클릭 (요소가 iframe 안에 있는경우에 대한 실습)
fr = driver.find_element_by_css_selector("#minime")
driver.switch_to_frame(fr)
driver.find_element_by_css_selector("#mail_count_profile").click()
time.sleep(2)
# 메일쓰기 버튼 클릭
driver.find_element_by_xpath('//*[@id="nav_snb"]/div[1]/a[1]').click()
time.sleep(2)


# 메일 작성
action = ActionChains(driver) #action 초기화
time.sleep(1)
(
    action.send_keys(receive_user).pause(2).send_keys(Keys.TAB).send_keys(Keys.TAB)
    .send_keys(mail_subject).pause(2).send_keys(Keys.TAB)
    .send_keys(mail_content).pause(2).perform()
)

# 보내기 버튼 클릭 
time.sleep(2)
driver.find_element_by_css_selector("#sendBtn").click()