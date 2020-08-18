# 가변 매개변수
# 한 함수에 한개만 허용된다. 
# 가변매개변수는 항상 가장 마지막에 위치한다. 

def 함수이름(매개변수1, 매개변수2, *가변매개변수):
	print(매개변수1)
	print(매개변수2)
	print(가변매개변수)

# 기본 매개변수
# 기본적으로 들어가는 매개변수 

def print_n_times(value, n=5):
	# n 번 반복합니다. 
	for i in range(n):
		print(value + str(i))

print_n_times("안녕하세요")