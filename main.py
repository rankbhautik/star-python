import turtle

col = ('yellow','red','green','orange','blue','white','red','blue')

t =turtle.Turtle()
screen =turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(100):
    t.color(col[i%5])
    t.forward(i*4)
    t.left(74)
    t.width(8)

