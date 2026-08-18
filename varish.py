import random

number = random.randint(1, 100)
attempts = 0

print("Number Guessing Game")
print("1 se 100 ke beech number guess karo!")

while True:
    guess = int(input("Apna guess: "))
    attempts += 1

    if guess < number:
        print("Thoda bada number try karo")
    elif guess > number:
        print("Thoda chhota number try karo")
    else:
        print(f"Sahi jawab! Number: {number}")
        print(f"Attempts: {attempts}")
        break

