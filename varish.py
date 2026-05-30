import random

score = 0

while True:

    roll = input("Roll the dice? (y/n): ")

    if roll.lower() == "y":

        number = random.randint(1, 6)
        print("You got:", number)

        score += number
        print("Current Score:", score)

    else:
        print("\nGame Ended")
        print("Final Score:", score)
        break