a , b = 10 , 20

print(a, b)

# 스왑
a, b = b, a

print(a, b)

for i, value in enumerate([1,2,3,4,5,6]):
	print(f" {i} 번쨰 값입니다. {value}")

# 튜플이 요소가 하나일 때 생성방법 

print((273, ))
print(type(273,))


# 딕셔너리의 키 값으로 튜플이 사용가능하다 

a = {
	(0,0) : 10,
	(0,1) : 20,
	(1,0) : 30,
	(1,1) : 40
}

# 튜플은 괄호를 생각 가능하다. 
print( a[(0,0)])