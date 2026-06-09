class BankAccount:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw ${amount}")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Current balance : ${self.balance}")            

    def view_transactions(self):
        if len(self.transactions) == 0:
            print("No transactins found.")
        else:
            for transaction in self.transactions:
                print(transaction)       

class BankSystem:
    def __init__(self):
        self.accounts = []

    def creat_account(self):
        name = input("Enter Name : ")
        password = input("Creat Password : ")

        account = BankAccount(name,password)
        self.accounts.append(account)

        print("Account Creat Successfully!")

    def login(self):
        name = input("Enter Name : ")
        password = input("Enter Password : ") 

        for account in self.accounts:
            if account.name == name and account.password == password:
                print(f"Welcome {name}")

                return account 

        print("Invalid Credentials!")  

    def view_all_accounts(self):
        if len(self.accounts) == 0:
            print("No Account Found.")
        else:
            for account in self.accounts:
                print(account.name)

bank = BankSystem()

while True:
    print("\n\033[1;92m==== BANK SYSTEM ====\033[0m")
    print("\033[1;93m")
    print("1. Creat Account")
    print("2. login")
    print("3. View All Account")
    print("4. Exit")
    print("\033[0m")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        bank.creat_account()

    elif choice == "2":
        user = bank.login() 

        if user:
            while True:
                print("\033[1;94m")
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Cheak Balance")
                print("4. Transaction History")
                print("5. logout")
                print("\033[0m")

                option = input("Enter Choice : ")
                if option == "1":
                    amount = float(input("Amount : "))
                    user.deposit(amount)

                elif option == "2":
                    amount = float(input("Amount : "))
                    user.withdraw(amount)

                elif option == "3":
                    user.check_balance()

                elif option == "4":
                    user.view_transactions()

                elif option == "5":
                    break                    

    elif choice == "3":
        bank.view_all_accounts()

    elif choice == "4":
        break  