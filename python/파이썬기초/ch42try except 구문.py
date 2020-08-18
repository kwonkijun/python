while True:
	try:
		# 예외가 발생 할 수 있는 가능성이 있는 코드
		print(float(input("> 숫자를 입력해주세요 : ")) ** 2)
		break
	except:
		# 예외가 발생 할 떄 수행할 코드
		print("숫자를 입력하세요!")


# 리스트에 담긴 데이터가 숫자인지 확인하는 예제

list_input_a = ["52", "273", "32", "스파이"]

list_number = []

for item in list_input_a:
	try:
		float(item)
		list_number.append(item)
	except:
		pass


