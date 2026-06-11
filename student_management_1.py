import random
import pandas as pd
class BankAccount:
    def __init__(self,name,account_number,balance,password):
        self.name = name
        self.acc_num = account_number
        self.balance = balance
        self.password = password
        
    def login(self):
        entered_password = input("\nEnter Password : ")
        if entered_password == self.password:
            print("\n    Login Successful\n")
            print("=== Welcome To SBI Bank ===")
            return True
        else:
            print("Wrong Password")
            return False

    def deposit(self,amount):
        self.balance += amount
        print(f"You Deposite RS - {amount}")
        print(f"Current Balance : RS - {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You Withdraw RS - {amount}")
            print(f"Current Balance : RS - {self.balance}")
        else:
            print("Insufficient Balance")

    def details(self):
        print(f"\nAccount Holder : {self.name}")
        print(f"Account Number : {self.acc_num}")
        print(f"Current Balance : Rs. {self.balance}")


# account list 
accounts = []
while True:
    print("\nSBI BANK")
    print("1. Creat Account")
    print("2. Login Account")
    print("3. All Show Account")
    print("4. Exit")

    main_choice = input("\nEnter Choice : ")

    if main_choice == "1":
        print("\n===== Creat Account =====")
        name = input("Enter Your Name : ")
        balance = int(input("Enter Opening Balance : "))
        password = input("Creat password : ")
        acc_num = random.randint(
            100000000,
            999999999)
        user = BankAccount(
            name,
            acc_num,
            balance,
            password
        )  
        accounts.append(user)
        print("Account Created Successfully")
        print(f"\nYour Account Number : {acc_num}")

    elif main_choice == "2":
        acc_number = int(input("\nEnter Account Number : "))
        found = False

        for user in accounts:
            if user.acc_num == acc_number:
                found = True

                if user.login():
                    while True:
                        print("\n====== Bank Menu ======\n")
                        print("What do you want to do? :")
                        print("1. Account Detail")
                        print("2. Deposit")
                        print("3. Withdraw")

                        
                        choice = input("\nEnter Choice : ")
                        if choice == "1":
                            user.details()
                            again = input("\nDo you want to Countinue?(yes/no) : ")
                            if again.lower() != "yes":
                                print("Thanks For Using SBI Bank")
                                break

                        elif choice == "2": 
                            amount = int(input("\nEnter Deposite Amount : \n"))
                            user.deposit(amount)
                            again = input("\nDo you want to Countinue?(yes/no) : ")
                            if again.lower() != "yes":
                                print("Thanks For Using Bank")
                                break
                        elif choice == "3":
                            amount = int(input("\nEnter Withdraw Amount : \n"))
                            user.withdraw(amount)      
                            again = input("\nDo you want to Countinue?(yes/no) : ")
                            if again.lower() != "yes":
                                print("\nThanks For Using SBI Bank")
                                break
                        else:
                            print("Wrong Choice..") 
            if found == False:
                print("\nAccount Not Found")
    elif main_choice == "3":
        if len(accounts) == 0:
           print("\nNo Account Found")
        else:
            data = {
                "Name" : [],
                "Account Number" : [],
                "Balance" : []
            }
            for user in accounts:
                data["Name"].append(user.name)
                data["Account Number"].append(user.acc_num)
                data["Balance"].append(user.balance)

            df = pd.DataFrame(data)
            print(df)    
    elif main_choice == "4":
        print("\nThanks For Using SBI Bank")
        break

    else:
        print("Invalid Choice")
    





