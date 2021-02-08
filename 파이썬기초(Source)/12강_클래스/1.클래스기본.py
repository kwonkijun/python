class Calculator:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def add(self):
		result = self.first + self.second
		return result

	def sub(self):
		result = self.first - self.second
		return result

	def mul(self):
		result = self.first * self.second
		return result
	
	def div(self):
		result = self.first * self.second
		return result

a = Calculator(1, 2)
b = Calculator(3, 4)

print(a.add())
print(b.add())

#클래스로 만든 객체를 인스턴스라고도 한다. 
#그렇다면 객체와 인스턴스의 차이는 무엇일까? 이렇게 생각해 보자. 
# a = Cookie() 이렇게 만든 a는 객체이다. 
# 그리고 a 객체는 Cookie의 인스턴스이다. 
# 즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를
#  관계 위주로 설명할 때 사용한다. 
# "a는 인스턴스"보다는 "a는 객체"라는 표현이 어울리며 
# "a는 Cookie의 객체"보다는 "a는 Cookie의 인스턴스"라는 
# 표현이 훨씬 잘 어울린다.
