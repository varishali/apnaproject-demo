import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("Rock, Paper, Scissors (or quit): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid Choice")
        continue

    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("Draw!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score: You {user_score} - {computer_score} Computer")

print("\nFinal Score")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")