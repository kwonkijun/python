# n! = 1 * 2* 3* 4* 5* .. n-1 * n

def factorial_1(n):
	변수 = 1
	for i in range(1, n+1):
		변수 *= i 
	return 변수

def factorial_2(n):
	if n == 0:
		return 1
	else:
		return n * factorial_2(n-1)

print(factorial_1(10))
print(factorial_2(10))

# 1 1 2 3 5 8 13 21 .. 

def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(20))

# 메모화 

메모 = {1 : 1, 2: 1}
def f(n):
	if n in 메모:
		return 메모[n]
	else:
		output = f(n-1) + f(n-2)
		메모[n] = output
		return output

print(f(40))

