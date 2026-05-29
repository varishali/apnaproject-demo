class BankAccount:
    total_accounts = 0

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.history = []

        BankAccount.total_accounts += 1
        self.account_number = BankAccount.total_accounts

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully")

    def withdraw(self, amount, pin):
        if pin != self.pin:
            print("Wrong PIN")
            return

        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            self.history.append(f"Withdraw ₹{amount}")
            print(f"₹{amount} withdrawn successfully")

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_history(self):
        print("\nTransaction History")
        for i in self.history:
            print("-", i)


user1 = BankAccount("Varish", 1234)

user1.deposit(5000)
user1.withdraw(1000, 1234)

user1.show_balance()
user1.show_history()