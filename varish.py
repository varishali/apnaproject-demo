def ask_question(question,answer):
    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct Answer!\n")
        return 1

    else:
        print("Wrong Answer!\n")
        return 0
    
score = 0

print("\n==== PYTHON QUIZ GAME ====")

score += ask_question(
    "1. python kiusne banai?",
    "guido van rossum"
)
score += ask_question(
    "2. 5+5 = ?",
    "10"
)
score += ask_question(
    "3. HTML ka full form ?",
    "hupertext merkup languages"
)
score += ask_question(
    "4. Python file extension ?",
    ".py"
)
score += ask_question(
    "5. AI ka full form ?",
    "artificial intelligence"
)

if score == 5:
    print("Excellent!")

elif score >=3:
    print("Good Job!")

else:
    print("Need Practice!")        