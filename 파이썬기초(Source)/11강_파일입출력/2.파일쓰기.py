f = open(r"C:\Users\스타트코딩\Desktop\main\python\파이썬기초(Source)\11강_파일입출력\2.파일쓰기_결과.txt", 'w')
f.write("파일입출력\n")
f.close() 

# 파일 이어쓰기 
f = open(r"C:\Users\스타트코딩\Desktop\main\python\파이썬기초(Source)\11강_파일입출력\2.파일쓰기_결과.txt", 'a')
f.write("정말로\n")
f.write("재미있는데요?\n")
f.close()