import csv

f = open(r"C:\Users\스타트코딩\Desktop\main\python\파이썬기초(Source)\11강_파일입출력\5.csv파일다루기_결과.csv", 'r')
# csvWriter = csv.writer(f)
# csvWriter.writerow([1, '유재석'])
# csvWriter.writerow([2, '박명수'])
# csvWriter.writerow([3, '정준하'])

csvReader = csv.reader(f)
for data in csvReader:
    print(data)
f.close()