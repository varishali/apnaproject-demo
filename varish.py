class Bank:
    def __init__(self, name ,balance):
        self.name = name
        self.balance = balance

        self.history = []

    def deposit(self):

        amount = float(input("Enter the amount to deposite : "))
        self.balance += amount
        self.history.append(f"Deposited : {amount}")
        print("Amount deposited successfully.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw : "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.history.append(f"withdrawn : {amount}")
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print(f"current balance : {self.balance}")

    def transaction_history(self):

        if len(self.history) == 0 :
            print("No transaction history available.")

        else:
            print("Transaction History :")        

            for item in self.history:
                print(item)

user1 = Bank("Varish", 10000)

while True:
    print("\n=====  WELCOME TO THE VR BANK  =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1 - 5) : ")
    if choice == "1":
        user1.deposit()

    elif choice == "2":
        user1.withdraw()     

    elif choice == "3":
        user1.check_balance()

    elif choice == "4":
        user1.transaction_history()

    elif choice == "5":
        print("Thanks for using VR Bank . ") 
        break

    else:
        print("Invalid Choice. Please try again.")            