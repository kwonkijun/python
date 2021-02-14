import random
number = []
while len(number) < 6:
    i = random.randint(1, 45)
    if not i in number:
        number.append(i)

print(number)