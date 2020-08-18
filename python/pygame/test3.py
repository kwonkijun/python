import turtle

x = int(input("원의중심(x좌표): "))
y = int(input("원의중심(y좌표): "))
radius = float(input("원의 반지름: "))

t = turtle.Turtle()

t.penup()
t.goto(x, y)
t.pendown()
t.circle(radius)
