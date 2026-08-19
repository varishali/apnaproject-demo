import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "Draw"
    
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if rules[user] == computer:
        return "Aap Jeete!"
    else:
        return "Computer Jeeta!"

def play():
    score = {"user": 0, "computer": 0}
    
    print("Rock, Paper, Scissors Game!")
    print("Exit karne ke liye 'quit' likhiye")

    while True:
        user_choice = input("\nApna choice daaliye (rock/paper/scissors): ").lower()
        
        if user_choice == "quit":
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Galat input! Sirf rock, paper ya scissors likhiye")
            continue
        
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        
        print(f"Computer ne choose kiya: {computer_choice}")
        print(f"Result: {result}")
        
        if result == "Aap Jeete!":
            score["user"] += 1
        elif result == "Computer Jeeta!":
            score["computer"] += 1
    
    print(f"\nFinal Score - Aap: {score['user']} | Computer: {score['computer']}")
    print("Game khatam!")

play()
