
import time 
t = time.localtime()
formatted_time = time.strftime (f"Date = {"%Y/%m/%d"} | time = {"%I:%M:%S %p"}")
print(formatted_time)



# account class

class Account:
    def __init__(self, acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

        # transaction history
        self.history = []

    def deposite(self):

        amount = int(input("Enter deposite amount : "))
        self.balance += amount
        self.history.append(f"Deposited : {amount}")

    def withdraw(self):

        amount = int(input("Enter withdraw amount : "))
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw : {amount}")
            print("Momey Withdrawn")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance : ",self.balance)

    def show_history(self):
        print("\n=== Transaction History ===")
        if len(self.history) == 0:
            print("No Transaction ")
        else:
            for item in self.history:
                print(item)
# bank class
class Bank:
    def __init__(self):
        self.accounts = []
        self.next_acc_no = 10001

    def create_account(self):

        acc_no = self.next_acc_no
        name = input("Enter Name : ")
        balance = int(input("Enter Initial Balance : "))
        print("Account Number : ",acc_no)
        # account object create
        account = Account(
            acc_no,
            name,
            balance
        )                                               
        # save object
        self.accounts.append(account)
        self.next_acc_no += 1
        print("Acount Created")

    def find_account(self,acc_no):
        for account in self.accounts:
            if account.acc_no == acc_no:
                return account
        return None

    def deposite_money(self):
        acc_no = int(input("Enter Account Number : "))
        account = self.find_account(acc_no)
        if account:
            account.deposite()
        else:
            print("Account Not Found")

    def withdraw_money(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)
        if account:
            account.withdraw()
        else:
            print("Account Not Found")

    def check_balance(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)
        if account:
            account.show_balance()
        else:
            print("Account Not Found")

    def transfer_money(self):
        sender_no = int(input("Sender Account : "))
        reciever_no = int(input("Reciever Account : "))
        amount = int(input("Enter Amount : "))

        sender = self.find_account(sender_no)
        reciever = self.find_account(reciever_no) 

        if sender and reciever:
            if amount <= sender.balance:
                sender.balance -= amount
                reciever.balance += amount
                sender.history.append(
                    f"Transferred {amount} to {reciever_no}"
                ) 
                reciever.history.append(
                    f"Recieved {amount} from {sender_no}"
                )     
                print("Transfer Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Accounts")  

    def transaction_history(self):
        acc_no = int(input("Enter Account No : ")) 
        account = self.find_account(acc_no)

        if account:
            account.show_history()

        else:
            print("Account Not Found")

# object create
bank = Bank()

# main program 
while True:
    print("\n====  BANK MANAGEMENT SYSTEM  ====")
    print("1. Create Account")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Transaction History")
    print("7. Exit")

    choice = input("Enter choice : ")

    # create account
    if choice == "1":
        bank.create_account()

    # deposite
    elif choice == "2":
        bank.deposite_money()

    # withdraw
    elif choice == "3":
        bank.withdraw_money()

    # check balance
    elif choice == "4":
        bank.check_balance()

    # transfer
    elif choice == "5":
        bank.transfer_money()

    # history
    elif choice == "6":
        bank.transaction_history()

    # exit
    elif choice == "7":
        print("Program Closed")
        break 

    else:
        print("Invalid Choice")        
