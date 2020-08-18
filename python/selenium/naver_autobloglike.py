# 주의 사항 
# 동일한 게시글에 공감/공감취소를 6회 이상 반복 시 더 이상 해당 게시글에 공감을 누를 수 없습니다. 
# 위 기준을 3회 반복할 경우, 비정상적인 이용자로 판단하여 7일간 공감 기능이 제한됩니다. (네이버)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyperclip
import time
import telepot

driver = webdriver.Chrome()
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
driver.implicitly_wait(3)
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

id ="kkj6369"
pw ="koC3848!!@"

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

# 블로그 홈으로 이동

page_num = 1 # 페이지 번호 
max_page_num = 10 # 페이지 당최대 이웃 새글 수 
url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
driver.get(url)

# 좋아요 버튼 클릭 새로운 페이지의 이웃새글의 수가 10개가 아닐 경우 종료. 
while True:
    time.sleep(10)
    off_btns = driver.find_elements_by_css_selector(".u_likeit_list_btn._button.off")
    
    if(len(off_btns) > 0):
        for off_btn in off_btns:
            off_btn.click()
            # 여기서 댓글 버튼을 클릭 
            time.sleep(5)
        page_num += 1
        url = f"http://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage={page_num}&groupId=0"
        driver.get(url)
    else:
        break

token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
mc = '1021336969'
bot = telepot.Bot(token)

bot.sendMessage(mc, "블로그 이웃 새글 좋아요 작업이 완료되었습니다.")