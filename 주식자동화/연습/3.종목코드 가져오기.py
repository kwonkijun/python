import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

print(codeList)
kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name

f = open(r'C:\Users\스타트코딩\Desktop\main\python\주식자동화\연습\kospi.csv', 'w')
for item in kospi.items():
    f.write(f'{item[0]},{item[1]}\n')
f.close()