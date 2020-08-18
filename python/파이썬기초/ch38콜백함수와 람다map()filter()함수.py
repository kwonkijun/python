def call_10_times(func):
	for i in range(10):
		# 콜백 함수 (callback)
		func(i)

def print_hello(number):
	print("안녕하세요", number)

call_10_times(print_hello)
call_10_times(lambda number: print("안녕하세요", number)) # 자동으로 return 키워드를 붙이는 결과가 나타난다. 

# filter함수

def 짝수만(number):
	return number % 2 == 0

짝수만 = lambda number: number % 2 == 0

a = list(range(100))
b = filter(짝수만, a)

def 제곱(number):
	return number * number

# map 함수는 기존의 리스트를 바탕으로 새로운 리스트를 만든다. 
a = list(range(100))
print(list(map(제곱, a)))

# map(), filter() 함수 등은 제너레이터 함수라서 내부의 데이터가 실제로 메모리에 용량을 차지하는 것들이 아닙니다.

# 리스트 내포를 위주로 사용하는 것이 좋다. 