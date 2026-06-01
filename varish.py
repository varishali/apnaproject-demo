import random

user = random.randint(1, 6)
computer = random.randint(1, 6)

print("You:", user)
print("Computer:", computer)

if user > computer:
    print("You Win!")
elif computer > user:
    print("Computer Wins!")
else:
    print("Draw!")