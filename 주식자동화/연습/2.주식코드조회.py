import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

# 표 10.1 CpStockCode 클래스의 주요 메소드

# CodeToName(code)	code에 해당하는 종목명을 반환	
# NameToCode(name)	name에 해당하는 종목코드을 반환	
# CodeToFullCode(code)	code에 해당하는 FullCode를 반환
# FullCodeToName(fullcode)	fullcode에 해당하는 종목명을 반환	
# FullCodeToCode(fullcode)	Fullcode에 해당하는 Code를 반환	
# CodeToIndex(code)	Code에 해당하는 Index를 반환	
# GetCount()	종목 코드 수를 반환	
# GetData(type, index)	해당 인덱스의 종목 데이터를 반환 (type - 0 : 종목코드, 1: 종목명, 2: FullCode)	

# 종목 코드의 전체 수
print(instCpStockCode.GetCount())

# 해당 인덱스의 종목 데이터를 반환
print(instCpStockCode.GetData(2, 0))

# 0 ~ 9 인덱스 종목명 출력
for i in range(0, 10):
    print(instCpStockCode.GetData(1,i))


# name 에 해당하는 종목명을 반환
naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)