while True:
	select = int(input("\n메뉴를 입력하세요 \n1. 게임시작 2. 랭킹보기 3. 게임종료 \n선택:"))
	if select == 1:
		print("=====게임을 시작합니다=====")
	elif select == 2:
		print("=====랭킹보기=====")
	elif select == 3:
		print("=====게임을 종료합니다=====")
		break
	else:
		print("다시 입력해 주세요")
