class Cat:
    foodAmount = 10
    def eatFood(self):
        Cat.foodAmount -= 1

cat1 = Cat()
cat2 = Cat()

print(cat1.foodAmount)
print(cat2.foodAmount)

cat1.eatFood()

print(cat1.foodAmount)
print(cat2.foodAmount)