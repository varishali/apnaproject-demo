print("\033[1m== WELCOME TO SMART ATM ==\033[0m")

pin = 12345
balance = 20000 
history = []
attempt = 0

while attempt < 3:
    user_pin = int(input("Enter pin : "))
    if user_pin == pin:
        print("\033[1m= Login Successfully =\033[0m")

        while True:
            print("\n== ATM MENU ==")
            print("1. Cheak balance")
            print("2. Deposite money")
            print("3. Withdraw money")
            print("4. Transaction history")
            print("5. Exit")

            choice = input("Enter your choice : ")

            #cheak balance
            if choice == "1":
                print(f"your balance is : {balance}")

            #deposite
            elif choice == "2":
                amount = int(input("Enter amount to deposite : "))
                balance += amount
                history.append(f"deposited {amount}")
                print(f"{amount} deposited successfuly.")
              
            

            elif choice == "3":
                amount = int(input("Enter amount to withdraw : "))
                balance -= amount
                history.append(f"withdraw {amount}")
                print(f"{amount} withdraw successful.") 


            # history
            elif choice == "4":
                if len(history) == 0:
                    print("No transectons yet.")  
                else:
                    print("transection history")

                    for i in history:
                        print(i)

            #exit
            elif choice == "5":
                print("Thanks for using SMART ATM")
                break


            else:
                print("Invalid choice.")

        break
    else:
        print("Invalid PIN")
                            
                             
                




