balance = 5000

print("welcome to ATTM ")

while True:
    print("1. cheak balance")
    print("2. deposite money")
    print("3. withdraw money")
    print("4. exit")

    choice = input("Enter choice(1-4):")

    if choice == "1":
        print("your balance is :",balance)

    elif choice == "2":
        amount = int(input("Enter diposite amount :"))
        balance = balance + amount
        print("money diposited succesfully")
        print("new balance :",balance)
        

    elif choice == "3":
        amount = int(input("Enter withdraw amount:"))
        if amount<=balance:
            balance = balance - amount
            print("please collect your cash:")
            print("remainning balance :",balance)

        else:
            print("Insufficient balance")

    elif choice == "4":
        print("thankyou for using ATM")
        break

    else:
        print("Invalid choice")            
















