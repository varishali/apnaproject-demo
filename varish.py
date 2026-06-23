balance = 1000

while True:

    print("\n===== BANK SYSTEM =====")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        amount = int(input("Enter Amount: "))

        balance += amount

        print("Deposit Successful!")

    elif choice == "2":

        amount = int(input("Enter Amount: "))

        if amount <= balance:

            balance -= amount

            print("Withdraw Successful!")

        else:

            print("Insufficient Balance!")

    elif choice == "3":

        print("Current Balance:", balance)

    elif choice == "4":

        print("Thank You!")

        break

    else:

        print("Invalid Choice!")
