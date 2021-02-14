class Cat:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def crying(self):
		print("미야옹!")

	def getName(self):
		return self.name

	def getAge(self):
		return self.age


class myCat(Cat):
	def crying(self):
		print("애용!")