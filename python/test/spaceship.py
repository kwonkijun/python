std_num = "12345678"
count = 0
try:
	a = int(input())
except:
	print("제대로된 숫자를 입력하세요")

for i in range(1, a * 2):
	if(i <= a):
		# 공백 출력
		for j in range(a-i):
			print(' ', end='')

		# 숫자 출력(1)
		for j in range(i):
			print(std_num[count], end='')	
			count = count + 1
			if(count % 8 == 0):
				count = 0
		# 사이 공백 출력
		blank = " " * a
		if i == a:
			blank = "*" * a

		print(blank, end='')
		# 숫자 출력 (2)
		for j in range(i):
			print(std_num[count], end='')	
			count = count + 1
			if(count % 8 == 0):
				count = 0
	else:
		# 공백 출력
		for j in range(i-a):
			print(' ', end='')
		# 숫자 출력(1)
		for j in range(a*2 - i):
			print(std_num[count], end='')	
			count = count + 1
			if(count % 8 == 0):
				count = 0
		# 사이 공백 출력
		blank = " " * a
		if i == a:
			blank = "*" * a

		print(blank, end='')
		# 숫자 출력 (2)
		for j in range(a*2 - i):
			print(std_num[count], end='')	
			count = count + 1
			if(count % 8 == 0):
				count = 0
	print()
	