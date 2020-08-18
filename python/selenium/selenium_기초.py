import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 

driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)

time.sleep(2)
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys('파이썬') 
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.ENTER)

driver.find_element_by_css_selector(".LC20lb.DKV0Md").click()
