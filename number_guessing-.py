import random

secret = random.randint(1, 100)
attempts = 0

print("Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter Number: "))
    attempts += 1

    if guess < secret:
        print("Too Low!")
    elif guess > secret:
        print("Too High!")
    else:
        print("Congratulations!")
        print(f"You guessed in {attempts} attempts")
        break