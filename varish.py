balance = 10000

while True:

    print("\n===== ATM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        print("Current Balance:", balance)

    elif choice == "2":

        amount = float(input("Enter Amount: "))

        if amount > 0:

            balance += amount

            print("Deposit Successful!")

        else:

            print("Invalid Amount!")

    elif choice == "3":

        amount = float(input("Enter Amount: "))

        if amount <= balance:

            balance -= amount

            print("Withdrawal Successful!")

        else:

            print("Insufficient Balance!")

    elif choice == "4":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")