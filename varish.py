import time
import random

questions = [
    ["Python kisne banayi?", "guido van rossum"],
    ["5 + 5 ?", "10"],
    ["India ki capital?", "delhi"],
    ["HTML ka full form?", "hypertext markup language"],
    ["AI ka full form?", "artificial intelligence"]
]


def ask_question(question,answer):
    print("You Have 15 Second !")
    start_time = time.time()
    user_answer = input(question + " ")
    end_time = time.time()
    total_time = end_time - start_time

    if total_time > 15:
        print("Time Out ! \n")
        return 0
    
    if user_answer.lower() == answer.lower():
        print("Correct Answer!\n")
        return 1

    else:
        print("Wrong Answer!\n")
        return 0
    
score = 0

print("\n=== Random Quiz Game ===")

random.shuffle(questions)

for q in questions:
    score += ask_question(q[0],q[1])

print("==== Final Score ====")
print("Your Score :",score, "/",len(questions))    