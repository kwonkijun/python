# False 로변환되는 것들
# bool()
# None 
# 0
# 0.0
# 빈 컨테이너 "" b"" - 빈 바이너리열 () {}


# pass 문 아무런 의미가 없고 나중에 입력하기 위함
number = 0 # 나중에!
if number != 0:
    pass
else:
    pass

# 1. 12 , 5 , 아무것도 출력 X
# 2. if 10 < x < 20: (파이썬에서 사용되는 범위 연산자)

# 3. 

year = int(input("태어난 해를 입력해주세요> "))

if year % 12 == 0:
    print("원숭이 띠 입니다.")
elif year == 1:
    print("닭 띠 입니다.")
elif year == 2:
    print("개 띠 입니다.")
elif year == 3:
    print("돼지 띠 입니다.")
elif year == 4:
    print("쥐 띠 입니다.")
elif year == 5:
    print("소 띠 입니다.")
elif year == 6:
    print("범 띠 입니다.")
elif year == 7:
    print("토끼 띠 입니다.")
elif year == 8:
    print("용 띠 입니다.")
elif year == 9:
    print("뱀 띠 입니다.")
elif year == 10:
    print("양 띠 입니다.")
elif year == 11:
    print("말 띠 입니다.")