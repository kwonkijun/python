try:
	#예외가 발생할 가능성이 있는 코드
	number = int(input("> 정수 입력"))
	print("입력 값은 {}입니다.".format(number))
except:
	#예외가 발생했을 경우 실행할 코드
	print("예외가 발생 했습니다. ")
finally:
	# 무조건 적으로 실행하는 코드
	print("무조건적으로 실행됩니다.")