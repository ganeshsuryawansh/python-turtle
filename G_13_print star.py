
from turtle import *
color('red', 'yellow')
bgcolor("black")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()