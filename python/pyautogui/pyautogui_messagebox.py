import pyautogui

btn_1 = pyautogui.alert(text = 'aaa', title='title', button='hello')
print(btn_1)
print(type(btn_1))

btn_2 = pyautogui.confirm(text='aaa', title='title', buttons=('사과', '당근'))
print(btn_2)

btn_3 = pyautogui.prompt(title='title', default='하고싶은말을 입력하세요.')
print(btn_3)

btn_4 = pyautogui.password('password', '비밀번호를 입력하세요', mask='$')
print(btn_4)