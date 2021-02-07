f = open(r"C:\Users\스타트코딩\Desktop\main\python\파이썬기초(Source)\11강_파일입출력\2.파일쓰기_결과.txt", 'r')
datas = f.readlines()
for data in datas:
    print(data)
f.close() 

