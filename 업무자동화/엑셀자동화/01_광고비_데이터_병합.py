# 비쥬얼 베이직 vs 파이썬
# 웹에 있는 데이터 크롤링
# -> 엑셀로 다운 받고
# -> 하나의 엑셀로 병합시키고 (VBA는 여기까지만 됨)
# -> 그리프로 시각화
# -> 보고서 만들고
# -> 이메일로 송신 (파이썬으로는 다가능)

import pandas as pd

company_list = ["LG전자", "삼성전자", "현대자동차"]

df_merge = pd.DataFrame() # 빈 데이터프레임생성

for company in company_list:
    df = pd.read_excel(rf"C:\Users\스타트코딩\Desktop\main\python\업무자동화\엑셀자동화\엑셀예제\2017년_광고비_{company}.xlsx")
    df.set_index("date", inplace=True) # df = df.set_index("date") 와 같은 기능
    df_merge[company] = df["total"] # df에 인덱스 이름이 없어도 만들어준다

print(df_merge)
df_merge.to_excel(r"C:\Users\스타트코딩\Desktop\main\python\업무자동화\엑셀자동화\01_광고비_데이터_병합.xlsx")