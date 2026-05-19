import random

print("\033[1;92m")
print("=" * 32)
print("      NUMBER GUESSING GAME")
print("=" * 32)
print("\033[0m")

secret_number = random.randint(1,100)

attempt = 0

while True:
    guess = int(input("\033[1;95mEnter Your Guess (1-100) : \033["))

    attempt += 1

    if guess > secret_number:
        print("\033[1;96mToo High!\033[0m")

    elif guess < secret_number:
        print("\033[1;91mToo Low!\033[0m")

    else:
        print("\033[1;93m")
        print(f"Correct Number : {secret_number}")
        print(f"You Guessed It In {attempt} Attempts.")
        print("\033[0m") 

        break       
