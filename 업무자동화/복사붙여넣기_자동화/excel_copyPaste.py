import win32com.client
import pyautogui as pg

# 상수 선언
MIN_ROW_NUM = 4
PATH = 'Users\kwonkijun\Desktop'

# 사용자 입력 데이터
company_name = pg.prompt(text='제약회사명을 입력하세요', title='Message', default='입력하세요')
sheet_name = pg.prompt(text='매입회사명을 입력하세요', title='Message', default='에스디메디칼/에스비약품')

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

print("data file max_row : ", max_row)
print("data list : ", data_list)
# 데이터 비교 후 붙여넣기 
path = rf'C:\{PATH}\{company_name}-origin.xls'
workbook_origin = excel.Workbooks.Open(path)
sheet = workbook_origin.Sheets(sheet_name)

max_row = find_max_row('origin')    
curr_row = max_row - 1
print("origin file max_row : ", max_row)

for data in data_list:
    print(data)
    is_exist_row = False
    # 데이터 형식 변경(날짜, 수량)
    date = data[0].replace("/", "-")
    count = int(data[2])
    while curr_row >= MIN_ROW_NUM:
        if sheet.Range(f'C{curr_row}').Value == data[1] :
            sheet.Range(f'A{curr_row}:Q{curr_row}').Copy()
            sheet.Range(f'A{max_row}').Insert()
            sheet.Range(f'A{max_row}').Value = date
            sheet.Range(f'G{max_row}').Value = count
            is_exist_row = True
            break
        curr_row = curr_row - 1
    if(not is_exist_row):
        sheet.Range(f'C{max_row}').Value = data[1]
        sheet.Range(f'A{max_row}').Value = date
        sheet.Range(f'G{max_row}').Value = count
    max_row = max_row + 1
    curr_row = max_row - 1 # 초기화
        

workbook_origin.SaveAs(rf'C:\{PATH}\{company_name}.xls')
excel.quit()