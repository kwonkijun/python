"""
구문오류 = syntax error
- 문법상 오류가 있을 때 나타나는 에러

예외 = Exception
- 문법상 오류는 없는데 실행 중에 나타나는 에러
- 런타임에러 
"""

while True:
	string_input = input("정수 입력>")
	if string_input.isdigit():
		number_input_a = int(string_input)
		print("원의 둘레: ", 2* 3.14 * number_input_a)
		break
	else:
		print("정수를 입력해주세요!")
