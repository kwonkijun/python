#- 스팸성 계정으로 판단하여 계정 정지를 먹이는 경우 
#– 과도한 팔로우를 하거나 너무 많은 언팔을 한 경우
#– 인스타그램이 아닌 타사 앱을 이용해 좋아요를 얻은 경우
#– 동일한 ‘댓글’을 여러 번 반복해 사용한 경우
#– 짧은 시간 과도한 좋아요를 한 경우
#– 짧은 시간 많은 게시물을 등록 한 경우


from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import quote_plus

from my_modules import reply_maker
import time
import pyautogui
import telepot
import pyperclip

insta_id = '01043521929'
insta_pw = 'koC3848!@#'

driver = webdriver.Chrome()
url = "https://www.instagram.com/accounts/login/?hl=ko"
driver.implicitly_wait(3)
driver.get(url)
action = ActionChains(driver)

# 로그인 
driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input").send_keys(insta_id)
time.sleep(1)
driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input").send_keys(insta_pw)
time.sleep(1)
driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()

# 로그인 휴대폰 확인
login_code = pyautogui.prompt(title='로그인코드', default='인스타그램 로그인코드를 입력하세요')
driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.gi2oZ > div > label > input").send_keys(login_code)
time.sleep(1)
driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.CovQj.jKUp7.iHqQ7 > button").click()
time.sleep(1)

# 알림 팝업 - 나중에하기 클릭
driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
time.sleep(3)

# 검색
keyword = quote_plus("좋아요반사")
url = f"https://www.instagram.com/explore/tags/{keyword}?hl=ko"
repeat_num = 2
while repeat_num > 0:
    print(3-repeat_num, "번째 작업")
    driver.get(url)

    recent_posts = driver.find_element_by_css_selector("#react-root > section > main > article > div:nth-child(3)")
    recent_posts = recent_posts.find_elements_by_css_selector(".eLAPa")

    max_num = 9
    for recent_post in recent_posts:
        if(max_num < 1): break
        recent_post.click()
        time.sleep(1)
        driver.find_element_by_css_selector(".wpO6b").click() # 좋아요 버튼 클릭
        time.sleep(1)
        driver.find_element_by_css_selector(".Ypffh").click() # 댓글 작성 부분 클릭 
        time.sleep(1)
        reply = reply_maker.make_reply_insta() # 댓글 내용 자동으로 만들기 
        action = ActionChains(driver)
        pyperclip.copy(reply)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(3)
        driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button").click() # 게시 버튼 클릭
        time.sleep(2)
        action = ActionChains(driver)
        action.send_keys(Keys.ESCAPE).perform()
        time.sleep(30)
        max_num -= 1

    repeat_num -= 1
    time.sleep(600)
    
token = '1083778601:AAEm90CkozJzDT2RzCQwjzWdMJ98ztvd9iY'
mc = '1021336969'
bot = telepot.Bot(token)

bot.sendMessage(mc, "인스타 자동 좋아요 + 좋아요 반사댓글 작업이 완료 되었습니다.")