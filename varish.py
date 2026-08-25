import turtle

t = turtle.Turtle()

t.speed(0)
colors = ['green','red','blue','yellow','pink','orange','black','white']
for i in range(100):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(59)
turtle.done()