import turtle, random

colors  = ["red","green","blue","orange","purple","pink","yellow"]

angle = int(input("회전각도를 입력하세요:"))
distance = int(input("이동간격을 입력하세요:"))
number = int(input("반복횟수를 입력하세요:"))

for i in range(number):
	color = random.choice(colors)
	turtle.color(color)
	turtle.colormode()
	turtle.circle(10 + i*5)
	turtle.setheading(-angle*i)
	turtle.penup()
	turtle.forward(distance)
	turtle.pendown()