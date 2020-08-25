import win32com.client
import pyautogui as pg

company_name = pg.prompt(text='제약회사명을 입력하세요', title='Message', default='입력하세요')

excel = win32com.client.Dispatch("Excel.Application")
path = rf'C:\Users\kwonkijun\Desktop\{company_name}.xls'
workbook = excel.Workbooks.Open(path)

sheet = workbook.Sheets('work')
totalNum = 0

try:
    for i in range(2, 5000):
        if(type(sheet.Range(f'D{i}').Value) != str):
            totalNum = i
            break;
except IndexError:
    pass
i = 3
while i <= (totalNum - 1):
    print(i)
    if(sheet.Range(f'I{i}').Value == sheet.Range(f'I{i-1}').Value): # 이름이 같고
        if(sheet.Range(f'D{i}').Value == sheet.Range(f'D{i-1}').Value): # 날짜가 같다면
            sheet.Range(f'K{i-1}').Value += sheet.Range(f'K{i}').Value # 수량 추가 *
            sheet.Range(f'O{i-1}').Value += sheet.Range(f'O{i}').Value # 공급금액 추가 *
            sheet.Range(f'P{i-1}').Value += sheet.Range(f'P{i}').Value # 세액금액 추가 *
            sheet.Range(f'Q{i-1}').Value += sheet.Range(f'Q{i}').Value # 합계금액 추가 *
            sheet.Rows(i).EntireRow.Delete() # 행 삭제 
            totalNum = totalNum - 1
        else:
            i = i + 1
    else:
        i = i + 1    
    
workbook.SaveAs(rf'C:\Users\kwonkijun\Desktop\{company_name}-data.xls')