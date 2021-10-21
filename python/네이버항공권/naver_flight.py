from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://flight.naver.com")

driver.find_elements_by_css_selector(".tabContent_option__2y4c6.select_Date__1aF7Y")[1].click()
