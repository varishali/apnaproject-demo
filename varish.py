import random

words = ["python", "apple", "computer", "coding", "school"]

word = random.choice(words)
guessed = ["_"] * len(word)

lives = 6

while lives > 0 and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Lives:", lives)

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        lives -= 1
        print("Wrong Guess!")

if "_" not in guessed:
    print("\nYou Win!")
    print("Word was:", word)
else:
    print("\nGame Over!")
    print("Word was:", word)