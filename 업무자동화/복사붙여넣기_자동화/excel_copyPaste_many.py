import win32com.client
import pyautogui as pg
import os

# 상수 선언
MIN_ROW_NUM = 4
DATA_PATH = 'Users\kwonkijun\Desktop\자동화\데이터'
ORIGIN_PATH = 'Users\kwonkijun\Desktop\자동화\원본'

# 거래처명(에스디메디칼)
# company_names = ['씨엠지제약', '남산메디칼', '넥스팜', '뉴젠팜', '동광제약', 
#                 '마더스제약', '명문바이오', '에이치엘비제약', '삼성제약', '삼익제약',
#                 '신신제약', '쓰리에스파마', '위더스제약', '지오엠디', '제이스팜', 
#                 '한국넬슨', '한국파마', '원화약품', '에스지메디언스', '파마킹', '미래제약']
# 거래처명(에스비약품)
company_names = ['경수약품', '고려제약', '구주제약', '남산메디칼', '넥스팜', '뉴젠팜', 
                '대원제약', '동광제약', '동국제약', '창조약품', '명문바이오', '미래제약',
                '삼성제약', '삼익제약', '신신제약', '에이치엘비제약', '에이프로젠', '오스코리아',
                '위더스제약', '인베스트팜', '조아제약', '조은약품', '조인포스씨엠지', '지오엠디',
                '제이스팜', '한국넬슨', '한국코러스', '한국파마', '동흥약품주식회사']
                
# 사용자 입력 데이터
sheet_name = pg.prompt(text='매입회사명을 입력하세요', title='Message', default='에스디메디칼/에스비약품')

for company_name in company_names:
    # 엑셀 객체 로딩
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible =True
    # 입력할 데이터 가져오기     
    path = rf'C:\{DATA_PATH}\{company_name}-data.xls'
    print(company_name)
    # 파일 있는지 확인 
    if(os.path.isfile(path)):    
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
            # 폰트 사이즈 변경
            sheet.Range(f'D{i}').Font.Size = 10
            sheet.Range(f'I{i}').Font.Size = 10
            sheet.Range(f'K{i}').Font.Size = 10
            date = sheet.Range(f'D{i}').Value # 날짜
            name = sheet.Range(f'I{i}').Value # 제품명
            count = sheet.Range(f'K{i}').Value # 수량
            data_list.append([date, name, count])

        print("data file max_row : ", max_row)
        print("data list : ", data_list)
        # 저장 후 종료
        workbook.Save()
        # 데이터 비교 후 붙여넣기 
        path = rf'C:\{ORIGIN_PATH}\{company_name}(자동화).xls'
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
                
        workbook_origin.Save()
        excel.quit()