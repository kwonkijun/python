import pyautogui

# position = pyautogui.locateCenterOnScreen('1.png')
# pyautogui.click(position)


# print(pyautogui.position())

pyautogui.screenshot('2.png', region=(1380,628,20,20))

position = pyautogui.locateCenterOnScreen('2.png')
pyautogui.click(position)