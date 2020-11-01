import pyautogui
import pyperclip
import time
import sys
import os
import win32com.shell.shell as shell

# 관리자 권한 얻어야 다른 프로그램 제어 가능
if sys.argv[-1] != 'asadmin':
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
    shell.ShellExecuteEx(
        lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

# 좌표
VENDER_POINT = {'x': 318, 'y': 245}  # 거래처명
NO_CONTENT_POP_POINT = {'x': 922, 'y': 609}  # 자료없음 팝업
GET_EXCEL_POINT = {'x': 616, 'y': 49}  # 엑셀저장
DONE_EXCEL_POINT = {'x': 1200, 'y': 466}  # 엑셀저장완료
FILE_PATH_POINT = {'x': 925, 'y': 369}  # 파일저장경로
FILE_SAVE_POINT = {'x': 1183, 'y': 862}  # 파일저장버튼

# 거래처명(에스디메디칼)
# VENDER_NAMES = ['씨엠지제약', '남산메디칼', '넥스팜', '뉴젠팜', '동광제약', 
#                 '마더스제약', '명문제약', '메디포럼', '삼성제약', '삼익제약',
#                 '신신제약', '쓰리에스파마', '위더스제약', '지오엠디코리아', '제이스팜', 
#                 '한국넬슨', '한국파마', '원화약품', '에스지메디언스', '파마킹', '미래제약']

# 거래처명(에스비약품)
VENDER_NAMES = ['경수약품', '고려제약', '구주제약', '남산메디칼', '넥스팜', '뉴젠팜', 
                '대원제약', '동광제약', '동국제약', '창조약품', '명문제약', '미래제약',
                '삼성제약', '삼익제약', '신신제약', '메디포럼', '에이프로젠', '오스코리아',
                '위더스제약', '인베스트팜', '조아제약', '조은약품', '조인포스씨엠지', '지오엠디',
                '제이스팜', '한국넬슨', '한국코러스', '한국파마', '동흥약품']

# 저장경로
FILE_PATH_NAME = '자동화'

# 이미지
NOT_FOUND_IMG = r'C:\Users\kwonkijun\Desktop\프로젝트(최신)\1.파이썬\업무자동화\엑셀다운로드자동화\not_found.Jpyautogui'

for VENDER_NAME in VENDER_NAMES:
    # 거래처명 검색
    pyautogui.moveTo(VENDER_POINT['x'], VENDER_POINT['y'], 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyperclip.copy(VENDER_NAME)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('f1')
    time.sleep(3)
    # 자료없음 팝업 삭제
    pyautogui.press('enter')

    # 엑셀다운
    pyautogui.moveTo(GET_EXCEL_POINT['x'], GET_EXCEL_POINT['y'], 0.5)
    pyautogui.click()
    time.sleep(1)
    # 파일이름변경
    pyperclip.copy(VENDER_NAME)
    pyautogui.hotkey('ctrl', 'v')
    # 파일경로변경
    pyautogui.moveTo(FILE_PATH_POINT['x'], FILE_PATH_POINT['y'], 0.5)
    pyautogui.click()
    pyperclip.copy(FILE_PATH_NAME)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    # 파일저장버튼
    pyautogui.moveTo(FILE_SAVE_POINT['x'], FILE_SAVE_POINT['y'], 0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(DONE_EXCEL_POINT['x'], DONE_EXCEL_POINT['y'], 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press('enter')