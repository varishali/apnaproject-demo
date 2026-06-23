score = 0

print("===== QUIZ GAME =====")

answer = input("Python Kisne Banayi? ")

if answer.lower() == "guido van rossum":

    score += 1

answer = input("2 + 2 = ")

if answer == "4":

    score += 1

answer = input("India Capital? ")

if answer.lower() == "delhi":

    score += 1

print("\nFinal Score:", score)
