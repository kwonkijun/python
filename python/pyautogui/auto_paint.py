import pyautogui
import time
import pyperclip

# 시작버튼 이동
pyautogui.moveTo(18, 1054,1)
pyautogui.click()
time.sleep(1)

# 그림판 검색 및 실행
pyperclip.copy('그림판')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

#pyautogui.screenshot('color_red.png', region=(860,56,10,10))
#pyautogui.screenshot('color_green.png', region=(926,56,10,10))
#pyautogui.screenshot('color_blue.png', region=(949,56,10,10))
#pyautogui.screenshot('color_yellow.png', region=(904,56,10,10))

#그림 그리기 
def pick_color(color_name):
    position = pyautogui.locateCenterOnScreen(f'{color_name}.png')
    pyautogui.moveTo(position.x, position.y, 1)
    pyautogui.click()

pick_color('color_red')

pyautogui.moveTo(300,300,1)
pyautogui.drag(0, 300,1, button='left')

pick_color('color_green')

pyautogui.moveTo(300,600,1)
pyautogui.drag(300, 0,1, button='left')

pick_color('color_blue')

pyautogui.moveTo(600,600,1)
pyautogui.drag(0, -300,1, button='left')

pick_color('color_yellow')

pyautogui.moveTo(600,300,1)
pyautogui.drag(-300, 0,1, button='left')

# 저장
time.sleep(1)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('my_drawling.png')
time.sleep(1)
pyautogui.press('enter')