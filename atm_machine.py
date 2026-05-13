print("\033[1mATM MACHINE\0330")

balance = 80000
pin = 1234

while True :
    user_pin = int(input("Enter your pin : "))

    if user_pin == pin:
        print("login succesful.")

        while True:
            print("1. Cheak balance")
            print("2. Deposite money")
            print("3. withdraw money")
            print("4. Exit")

            choice = input("Enter your choice : ")

            if choice == "1":
                print("your balance",balance)

            elif choice == "2":
                amount = int(input("enter deposite amount : "))
                balance += amount
                print("money deposited")
                print("new balance",balance)

            elif choice == "3":
                amount = int(input("enter withdraw money : "))
                if amount <= balance:
                    balance -= amount
                    print("please collect cash.")
                    print("remaining balance",balance)

                else:
                    print("insufficiant balance.")  

            elif choice == "4":
                print("Thank you.")
                break
            else:
                ("invalid choice")
        break   
    else:
        print("wrong pin.")     