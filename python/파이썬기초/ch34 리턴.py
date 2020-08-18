# 확인 문제 1 

def f_1(x):
	return 2*x + 1

def f_2(x):
	return (x**2) + (2 *x) + 1

print(f_1(10))
print(f_2(10))

def mul(*values):
	변수 = 1
	for i in values:
		변수 *= i
	return 변수

print(mul(5, 7, 9, 10))