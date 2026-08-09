import random

while True:
    input("Press Enter To Roll Dice...")
    roll = random.randint(1, 6)
    print(f"You Rolled : {roll}")
    
    again = input("Roll Again? (y/n) : ")
    if again.lower() != 'y':
        print("Game Over!")
        break