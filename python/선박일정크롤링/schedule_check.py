import time
import pyautogui, pyperclip

from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

origin = 'BUSAN'
destination = 'JEBEL ALI'

url = 'https://www.oocl.com/eng/Pages/default.aspx'

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

time.sleep(2)

# Click Accept 
driver.execute_script("acceptCookiePolicy();")

# Click Schedule
driver.find_element_by_xpath('//*[@id="tablist1-tab2"]').click()

time.sleep(2)

# Select Origin
driver.find_element_by_xpath('//*[@id="txt_auto_original"]').send_keys(Keys.ENTER)
pyperclip.copy(origin)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('down')
pyautogui.press('enter')

# Select Destination
time.sleep(2)
driver.find_element_by_xpath('//*[@id="txt_auto_destination"]').click()
pyperclip.copy(destination)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(2)
# window change
# prints parent window title
print("Parent window title: " + driver.title)
# get current window handle
p = driver.current_window_handle
# get first child window
chwnd = driver.window_handles
for w in chwnd:
	# switch focus to child window
	if(w!=p):
		driver.switch_to.window(w)
		break
time.sleep(0.9)
print("Child window title: " + driver.title)

# Excel down
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div[2]/div[1]/div[1]/a[2]/button")))
element.click()