import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Turtle Car Racing")

# Player
player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.penup()
player.goto(0, -250)

# Enemy
enemy = turtle.Turtle()
enemy.shape("turtle")
enemy.color("red")
enemy.penup()
enemy.goto(random.randint(-300, 300), 250)

score = 0

# Score
text = turtle.Turtle()
text.color("white")
text.penup()
text.hideturtle()
text.goto(-350, 250)

def show_score():
    text.clear()
    text.write(
        f"Score: {score}",
        font=("Arial", 18, "bold")
    )

show_score()

# Movement
def left():
    player.setx(player.xcor() - 30)

def right():
    player.setx(player.xcor() + 30)

screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Game
while True:

    enemy.sety(enemy.ycor() - 5)

    if enemy.ycor() < -300:
        enemy.goto(
            random.randint(-300, 300),
            300
        )
        score += 1
        show_score()

    # Collision
    if player.distance(enemy) < 30:
        text.goto(0, 0)
        text.write(
            "GAME OVER!",
            align="center",
            font=("Arial", 30, "bold")
        )
        break

    screen.update()

screen.mainloop()