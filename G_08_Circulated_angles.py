
import turtle
wb=turtle.Screen()
wb.bgcolor("black")
a=turtle.Turtle()
a.speed(0)
a.pencolor("red")
a.pensize(1)
x=0
while x<650:
    a.forward(2+x)
    a.right(90.899)
    x=x+1

wb.exitonclick()
