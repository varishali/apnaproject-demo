import turtle

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(5)

colors = ['lightblue','lightgreen','lightpink','lightyellow']

for i in range(20):
    screen.bgcolor(colors[i % 4])
    t.circle(50)
    t.left(20)

turtle.done()    