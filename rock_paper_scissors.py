import random

print("\033[1;92m")
print("=" * 34)
print("     ROCK PAPER SCISSORS GAME")
print("=" *34)
print("\033[0m")

choices = ["rock","paper","scissors"]

while True:
    user = input("\033[1;93mEnter Rock, Paper, or Scissors : \033[0m").lower()

    computer = random.choice(choices)

    print(f"\n\033[1;94mComputer Chose : {computer}\033[0m")

    if user == computer:
        print("\033[1;94mIt's a Draw!\033[0m")

    elif (
        (user == "rock" and computer == "scissers")or
        (user == "paper" and computer == "rock")or
        (user == "scissers" and computer == "paper")
    ):
        print("\033[1;94mYou Win!\033[0m")

    elif user in choices :
        print("\033[1;91mComputer Wins!\033[0m")    

    else:
        print("\033[1;94mInvalid Input!\033[0m")

    play_again = input("\033[1;94mPlay Again ? (yes/no) : \033[0m").lower()

    if play_again != "yes":
        print("\n\033[3;95mThanks For Playing.\033[0m ")

        break       