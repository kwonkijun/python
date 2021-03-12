import pyautogui
import time

# 3초 기다리기
time.sleep(3)

# 좌표 객체를 얻기
position = pyautogui.position()

# x, y 좌표
print(position.x)
print(position.y)
