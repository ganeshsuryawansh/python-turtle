
import turtle

n = 50
pen = turtle.Turtle()

for i in range(n):
    pen.color("red")
    pen.forward(i * 10)
    pen.right(144)
# closing the instance
turtle.done()