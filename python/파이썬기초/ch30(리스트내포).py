# 리스트 내포와 반복문

array = []
for i in range(0, 20, 2):
	array.append(i*i)

array = [i*i for i in range(0,20,2)]
print(array)

array_1 = [i for i in range(10)]
array_2 = [i for i in range(0, 10, 2)]
array_3 = [1 for i in range(10)]

# 리스트 내포와 조건문

array_1 = [i for i in range(10) if i % 3 ==0]


# 2 10진수와 2진수 변환

print("{:b}".format(12)) # 2진수 변환
# >>> 1100

int("1100", 2) # 10진수 변환 
# >>> 12

"안녕한녕하세요".count("안")

# 연습문제 
output = [i for i in range(1, 100+1) if "{:b}".format(i).count('0') == 1]

for item in output:
	print(" {} : {:b}".format(item, item))

print("합계 : {}".format(sum(output)))