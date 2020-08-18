print(max([273, 53, 32, 57, 103]))
print(min([273, 53, 32, 57, 103]))

print(max(273, 53, 32, 57, 103))
print(min(273, 53, 32, 57, 103))

print(sum([273, 53, 32, 57, 103]))

a = [0, 1, 2, 3, 4, 5]
reversed_a = reversed(a)
print(list(reversed_a))
print(list(reversed_a))

for i in reversed(a):
    print(i, end=" ")

a = [273, 103, 52, 32, 57]

for (i, element) in enumerate(a):
    print(f"{i}, {element}")

a = {
    "key_1" : "value_1",
    "key_2" : "value_2",
    "key_3" : "value_3",
}

for key, value in a.items():
    print(f"{key}키의 값은 {value}입니다. ")


"""
* 리스트에 적용할 수 있는 기본 함수 : min(), max(), sum()

# 일회용함수 : 제너레이터
* 리스트 뒤집기 : reversed()
* 현재 인덱스가 몇 번째인지 확인하기: enuerate()
* 딕셔너리로 쉽게 반복문 작성하기: items()

"""