import random

while True:

    roll = input("Roll the dice? (y/n): ")

    if roll == "y":
        number = random.randint(1, 6)
        print("You got:", number)

    else:
        print("Game Ended")
        break