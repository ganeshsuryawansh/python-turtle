
import turtle

t = turtle.Turtle()

s = 200
col = "red"
t.fillcolor(col)
t.begin_fill()
for _ in range(5):
    t.forward(s)
    t.right(144)

t.end_fill()
