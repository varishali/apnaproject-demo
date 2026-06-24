class ATM:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self):

        amount = int(input("Enter Amount : "))
        self.balance += amount
        print("Amount Deposited ..")
        print(f"Total amount is : {self.balance}")

    def withdraw(self):

        amount = int(input("Enter Amount To Withdraw : "))

        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdraw Successfully")
            print(f"Total Amount Is : {self.balance}")
        else:
            print("Insufficient Amount")

    def cheak_balance(self):
        print("Current Balance : ",self.balance)                

atm = ATM(1000)

while True:
    print("==  ATM MENU  ==")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Cheak Balance")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        atm.deposit()

    elif choice == "2":
        atm.withdraw()

    elif choice == "3":
        atm.cheak_balance()

    elif choice == "4":
        print("Thank You")
        break             
    else:
        print("Invalid Choice")