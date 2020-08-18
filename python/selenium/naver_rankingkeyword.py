from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 키 입력을 받기위한 모듈 
import os
import time

# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT

# 반복횟수 
REPEAT_NUM = 3
PORT = 9050

# Tor 및 Proxy 설정

while(REPEAT_NUM > 0):
    torexe = os.popen(r'C:\Users\Administrator\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = f"socks5://localhost:{PORT}" # IP:PORT or HOST:PORT
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(options=options)
    driver.get('http://check.torproject.org')
    time.sleep(3)
    new_ip = driver.find_element_by_css_selector('body > div.content > p:nth-child(3) > strong')
    print(new_ip.text)
    time.sleep(5)
    driver.quit()
    REPEAT_NUM = REPEAT_NUM - 1

# while(repeat_num > 0):
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get("https://www.naver.com")

#     time.sleep(5)

#     driver.find_element_by_css_selector("#query").send_keys('차이나 게이트')
#     driver.find_element_by_css_selector("#query").send_keys(Keys.ENTER) 

#     time.sleep(3)
#     driver.quit()
#     repeat_num = repeat_num - 1

#C:\Users\Administrator\Desktop\Tor Browser\Browser\TorBrowser\Tor