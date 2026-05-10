#number guessing game

import random

print("== welcome to number guessing game ==")

number = random.randint(1, 10)
   
guess = int(input("Guess a number between 1 to 10 : "))

if guess == number:
    print("correct guess!")
    print("you win!")

else:
    print("wrong guess")
    print(f"correct number was = {number}")    

















