import pyautogui

# 마우스 이동 (x 좌표, y 좌표, 이동시간)
pyautogui.moveTo(984,85,1)

# 마우스 클릭
# pyautogui.click()

# 마우스 2초간격으로 2번 클릭
pyautogui.click(clicks=1, interval=1)

pyautogui.moveTo(450, 405, 1)

# 드래그 하기
pyautogui.drag(0, 300, 1, button='left')
pyautogui.drag(300, 0, 1, button='left')
pyautogui.drag(0, -300, 1, button='left')
pyautogui.drag(-300, 0, 1, button='left')