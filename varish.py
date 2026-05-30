score = 0

questions = {
    "India ki capital kya hai? ": "delhi",
    "2 + 2 kitna hota hai? ": "4",
    "Python kis type ki language hai? ": "programming"
}

for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

print("\nFinal Score:", score, "/", len(questions))