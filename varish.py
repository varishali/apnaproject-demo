class BankAccount:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print("Money Deposited Successfully!")

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw ₹{amount}")
            print("Money Withdrawn Successfully!")

        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_transactions(self):

        if len(self.transactions) == 0:
            print("No Transactions Yet!")

        else:

            print("\nTransaction History:")

            for transaction in self.transactions:
                print(transaction)


user = BankAccount("Varish", "1234")

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        amount = float(input("Enter Amount: "))
        user.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter Amount: "))
        user.withdraw(amount)

    elif choice == "3":

        user.check_balance()

    elif choice == "4":

        user.show_transactions()

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")