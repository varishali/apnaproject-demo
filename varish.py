import random

while True:

    print("\n===== OTP Generator =====")
    print("1. Generate OTP")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        otp = random.randint(100000, 999999)

        print("\nYour OTP:", otp)

    elif choice == "2":
        break

    else:
        print("Invalid Choice!")