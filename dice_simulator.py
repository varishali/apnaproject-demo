import numpy as np

while True:
    dice = np.random.randint(1,7)
    print("Number --> ",dice)

    again = input("Do you want to Roll Again? yes/no : ")

    if again == "no":
        break

    