import pyautogui
import time

position = pyautogui.position() # 현재 위치의 x, y 값을 가져온다. 

pyautogui.moveTo(500,500) 
pyautogui.moveTo(500,500,2)

pyautogui.moveRel(0,300,2) # 2초동안 현재 위치에서 아래로 300만큼 이동한다. 

pyautogui.click()
pyautogui.click(clicks=2, interval=2) #클릭한번하고 2초있다가 클릭한번 한다.
pyautogui.doubleClick()

time.sleep(1)
pyautogui.typewrite('Hello')
pyautogui.typewrite(['enter']) # 어떠한 키를 누르는지 ['']안에 넣어 준다. 
