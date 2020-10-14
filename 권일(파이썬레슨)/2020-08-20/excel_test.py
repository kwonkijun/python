from openpyxl import Workbook

# 엑셀객체 생성
write_wb = Workbook()

# 엑셀시트 생성
write_ws = write_wb.create_sheet('실시간검색상위종목')

# 셀에 데이터 입력
write_ws['A1'] = "삼성전자"

# 행단위로 입력
write_ws.append(['LG전자', '250000', 'up', '2000'])

write_wb.save(r'C:\Users\kwonkijun\Desktop\프로젝트(최신)\파이썬\권일(파이썬레슨)\2020-08-20\실시간종목.xlsx')
