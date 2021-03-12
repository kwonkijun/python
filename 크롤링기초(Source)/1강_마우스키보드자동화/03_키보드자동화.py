import pyautogui
import time
import pyperclip

# 마우스 이동
pyautogui.moveTo(521,144,1)

# 마우스 클릭
pyautogui.click()

# 키보드 입력 
# pyautogui.write("i'am a automatic-robot", interval=0.1)

# pyautogui.press('enter')

# pyautogui.write("please use a lot", interval=0.1)

# 한글 입력

# 클립보드에 복사하기
pyperclip.copy("한글입력 되나요?")

# 붙여넣기
# pyautogui.keyDown("ctrl")
# pyautogui.press("v")
# pyautogui.keyUp("ctrl")

pyautogui.hotkey("ctrl", "v")