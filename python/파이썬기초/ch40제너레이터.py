def function_A():
	print("출력A")
	print("출력B")
	yield 100

generator = function_A()

value = next(generator)
print(value)


def 함수():
	print("출력A")
	yield 100
	print("출력B")
	yield 200
	print("출력C")
	yield 300
	print("출력D")
	yield 400

제너레이터 = 함수()
next(제너레이터)
next(제너레이터)
next(제너레이터)
next(제너레이터)


# 확인문제 1.
numbers = [1,2,3,4,5,6]
print("::".join(map(str, numbers)))

# 확인문제 2. 
numbers = list(range(1, 10 + 1))
print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 == 1, numbers)))
print()
print("# 3 이상, 7미만 추출하기")
print(list(filter(lambda x: 3 <= x < 7, numbers)))
print()
print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: (x ** 2) < 50, numbers)))


