# 영화추가

# 영화삭제

movie_list = []

while True:
    select = int(input('메뉴를 선택해 주세요 : (1) 영화 추가 (2) 영화 삭제 (3) 영화 목록 확인 (4) 프로그램 종료'))
    if(select == 1):
        print("영화 추가 메뉴를 선택했습니다.")
        movie_name = input('영화이름을 입력해 주세요:')
        movie_list.append(movie_name)
        print(f"영화 {movie_name} 추가되었습니다.")
    elif(select == 2):
        print("영화 삭제 메뉴를 선택했습니다.")
        # 직접 구현해 보세요.
        i = 1
        print("------영화 목록------")
        for movie in movie_list:
            print(f'{i}.{movie}')
            i = i + 1
        print("--------------------")
        deleteNum = int(input('삭제 하고 싶은 영화 영화 번호를 입력하세요 : '))
        del movie_list[deleteNum-1]
        print("삭제 됬습니다.")
    elif(select == 3):
        print("영화 목록 메뉴를 선택했습니다.")
        print("------영화 목록------")
        for movie in movie_list:
            print(movie)
        print("--------------------")
    elif(select == 4):
        print("프로그램을 종료합니다.")
        break
    