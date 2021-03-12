import pyautogui

# prompt = 입력창

keyword = pyautogui.prompt(text="검색어를 입력하세요")

print(type(keyword))