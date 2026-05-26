import numpy as np

lottery = np.random.randint(1,11)

user = int(input("Guess Number (1-10) : "))

if user == lottery:
    print("You Win!")
else:
    print("You Lose!")
    print("Wining Number : ",lottery)    