import time
from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.google.com/travel/flights?tfs=CBwQARopag0IAhIJL20vMDF2c2tuEgoyMDIxLTEwLTEzcgwIBBIIL20vMDNfM2QaKWoMCAQSCC9tLzAzXzNkEgoyMDIxLTEwLTE3cg0IAhIJL20vMDF2c2tucAGCAQsI____________AUABSAGYAQE&hl=ko'
driver.get(url)

time.sleep(2)
driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input").click()
