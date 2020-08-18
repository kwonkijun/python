import win32com.client
import pyautogui as pg

company_name = pg.prompt(text='제약회사명을 입력하세요', title='Message', default='입력하세요')

excel = win32com.client.Dispatch("Excel.Application")
path = rf'C:\Users\kwonkijun\Desktop\프로젝트(최신)\업무자동화\복사붙여넣기_자동화\{company_name}-data.xls'
workbook = excel.Workbooks.Open(path)

sheet = workbook.Sheets('work')

date = sheet.Range('D2').Value # 날짜
name = sheet.Range('I2').Value # 제품명
count = sheet.Range('K2').Value # 수량

print(date, name, count)

path = rf'C:\Users\kwonkijun\Desktop\프로젝트(최신)\업무자동화\복사붙여넣기_자동화\{company_name}-origin.xlsx'
workbook_origin = excel.Workbooks.Open(path)
sheet = workbook_origin.Sheets('에스디메디칼')
max_row = 0
for i in range(3, 5000):
    if(sheet.Range(f'B{i}').Value == None): 
        print(i)
        max_row = i 
        break
curr_row = max_row
while curr_row >= 4:
    if sheet.Range(f'C{curr_row}').Value == name :
        sheet.Range(f'A{curr_row}:P{curr_row}').Copy()
        sheet.Range(f'A{max_row}').Insert()
        max_row = max_row + 1
        break
    curr_row = curr_row - 1

workbook_origin.SaveAs(rf'C:\Users\kwonkijun\Desktop\프로젝트(최신)\업무자동화\복사붙여넣기_자동화\{company_name}-origin-result.xlsx')
excel.quit()