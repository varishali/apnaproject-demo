# Typing Speed Checker

import time

sentence = "python is easy"

print(sentence)

start = time.time()

typed = input("Type Here : ")

end = time.time()

if typed == sentence:
    print("Correct")

    print("Time :", round(end - start, 2), "seconds")

else:
    print("Wrong Typing")