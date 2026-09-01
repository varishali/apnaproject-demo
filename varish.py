import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

# Turtle create karo
t = turtle.Turtle()
t.speed(2)
t.color("blue")

# Square banao
for i in range(4):
    t.forward(100)
    t.right(90)

screen.exitonclick()  # Click karne pe window band hogi