import pandas as pd
from pandas import ExcelWriter

writer = ExcelWriter(r"C:\Users\스타트코딩\Desktop\main\python\업무자동화\엑셀자동화\02_장례식장_데이터_병합.xlsx")

"""
    판다스에서 기본으로 제공하는 엑셀함수는 기능이 제한적이다
    제대로 동작하지 않을 가능성이 있다
    
    -> ExcelWriter라는 모듈을 불러와서 탑재해 준다
"""

for year in range(2017, 2021):
    df = pd.read_excel(rf"C:\Users\스타트코딩\Desktop\main\python\업무자동화\엑셀자동화\엑셀예제\장사시설현황_2017년_2020년-20210221T015453Z-001\장사시설현황_2017년_2020년\{year}년 장사시설 현황\전국장사시설현황.xlsx", sheet_name="장례식장 시설정보")
    df = df[["시설명", "주소"]] # 두개 이상의 열을 가져오려면 리스트 자료형을 넣어 주면 된다
    df.to_excel(writer, sheet_name=f"{year}년")
    print(f"{year}년 데이터 병합 완료")

writer.save()