import win32com.client
import pyautogui as pg

# 상수 선언
MIN_ROW_NUM = 4
PATH = 'Users\kwonkijun\Desktop\프로젝트(최신)\파이썬\업무자동화\복사붙여넣기_자동화'

# 사용자 입력 데이터
company_name = pg.prompt(text='제약회사명을 입력하세요', title='Message', default='입력하세요')

# 입력할 데이터 가져오기 
excel = win32com.client.Dispatch("Excel.Application")
path = rf'C:\{PATH}\{company_name}-data.xls'
workbook = excel.Workbooks.Open(path)
sheet = workbook.Sheets('work')

# 데이터 리스트
data_list = []

def find_max_row(option):
    curr_row = 0
    if(option == 'data'):
        for i in range(2, 5000):
            if(sheet.Range(f'D{i}').Value == None): 
                curr_row = i 
                return curr_row
    elif(option == 'origin'):
        for i in range(3, 5000):
            if(sheet.Range(f'B{i}').Value == None): 
                curr_row = i 
                return curr_row

max_row = find_max_row('data')
for i in range(2, max_row):
    date = sheet.Range(f'D{i}').Value # 날짜
    name = sheet.Range(f'I{i}').Value # 제품명
    count = sheet.Range(f'K{i}').Value # 수량
    data_list.append([date, name, count])

# 데이터 비교 후 붙여넣기 
path = rf'C:\{PATH}\{company_name}-origin.xlsx'
workbook_origin = excel.Workbooks.Open(path)
sheet = workbook_origin.Sheets('에스디메디칼')

max_row = find_max_row('origin')    
curr_row = max_row

for data in data_list:
    while curr_row >= MIN_ROW_NUM:
        if sheet.Range(f'C{curr_row}').Value == data[1] :
            sheet.Range(f'A{curr_row}:P{curr_row}').Copy()
            sheet.Range(f'A{max_row}').Insert()
            # 데이터 형식 변경(날짜, 수량)
            date = data[0].replace("/", "-")
            count = int(data[2])
            sheet.Range(f'A{max_row}').Value = date
            sheet.Range(f'G{max_row}').Value = count
            max_row = max_row + 1
            break
        curr_row = curr_row - 1

workbook_origin.SaveAs(rf'C:\{PATH}\{company_name}-origin-result.xlsx')
excel.quit()