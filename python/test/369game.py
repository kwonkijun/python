# 3 6 9 게임

def checkAnswer(number):
	a = str(number)
	total = 0
	total += a.count('3')
	total += a.count('6')
	total += a.count('9')
	return total


for i in range(100):
	print(checkAnswer(i))

	

