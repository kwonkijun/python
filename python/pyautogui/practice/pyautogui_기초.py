# 공식문서 
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# pip install pyautogui
import pyautogui
import time

# 1. 마우스 이동 함수
# moveTo(x좌표 , y좌표, 시간)
pyautogui.moveTo(500, 100, 0.5)
# moveRel 현재 마우스 좌표 기준으로 이동 
pyautogui.moveRel(500, 100)

# 2. 마우스 클릭 함수
time.sleep(3)
pyautogui.click()
time.sleep(3)
pyautogui.doubleClick()
time.sleep(3)
pyautogui.rightClick()
pyautogui.click(clicks=3, interval=3)

# 3. 마우스 현재 좌표 확인하기
position = pyautogui.position()

# 4. 키보드 입력

pyautogui.typewrite('Hello', 0.4)
pyautogui.press('enter')
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')
pyautogui.hotkey('alt', 'f4')
