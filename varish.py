class User:
    def __init__(self,name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

class Account:
    next_acc_no = 10001

    def __init__(self,user, balance, pin):

        self.user = user

        self.acc_no = Account.next_acc_no
        Account.next_acc_no += 1

        self.balance = balance
        self.pin = pin

        self.history = []

    def deposit(self):
        amount = int(input("Enter Amount : "))
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        print("Money Deposited")

    def withdraw(self):
        amount = int(input("Enter Amount : "))

        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw ${amount}")
            print("Money Withdrawn")
        else:
            print("insufficient Balance")

    # balance
    def check_balance(self):
        print("Current Balance :",self.balance)

    # history
    def transaction_history(self):
        print("\n====  TRANSACTIONS  ====")
        if len(self.history) == 0:
            print("No Transaction")
        else:
            for item in self.history:
                print(item)

    # details           
    def show_details(self):       
        print("\n====  ACCOUNT DETAILS  ====")
        print("Account Number :",self.acc_no)
        print("Nmae :",self.user.name) 
        print("Age :",self.user.age)
        print("Mobile :",self.user.mobile) 
        print("Balance :",self.balance)                      

class Bank:
    def __init__(self):

        self.accounts = []

    # create Account
    def create_account(self):
        print("\n==== CREATE ACCOUNT ====")

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        mobile = input("Enter Mobile No : ")
        balance = int(input("Enter Opening Balance : "))
        pin = input("Set 4 Digit Pin :")

        user = User(name,age,mobile)

        account = Account(user,balance,pin)    
        self.accounts.append(account)
        print("\nAccount Created Successfully")
        print("Account Number :",account.acc_no)

    # find account
    def find_account(self,acc_no):

        for account in self.accounts:
            if account.acc_no == acc_no:
                return account

        return None

    # deposit
    def deposit_money(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)

        if account:
            account.deposit()

        else:
            print("Accounr Not Found")         

    # withdraw
    def withdraw_money(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)

        if account:
            account.withdraw()
        else:
            print("Account Not Found")

    # balance
    def check_balance(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)

        if account:
            account.check_balance()

        else:
            print("Account Not Found")     

    # show details
    def show_account(self):
        acc_no = int(input("Enter Account Number : "))

        account = self.find_account(acc_no)

        if account:
            account.show_details()

        else:
            print("Account Not Found")

    # transaction history
    def history(self):
        acc_no = int(input("Enter Account No : "))
        account = self.find_account(acc_no)                
        if account:
            account.transaction_history()

        else:
            print("Account Not Found")    


    # Transfer Money


    def transfer_money(self):

        sender_no = int(input("Sender Account Number : "))
        receiver_no = int(input("Receiver Account Number : "))
        amount = int(input("Enter Amount : "))

        sender = self.find_account(sender_no)
        receiver = self.find_account(receiver_no)

        if sender and receiver:

            if amount <= sender.balance:

                sender.balance -= amount
                receiver.balance += amount

                sender.history.append(
                    f"Transferred ₹{amount} to A/C {receiver.acc_no}"
            )

                receiver.history.append(
                    f"Received ₹{amount} from A/C {sender.acc_no}"
            )

                print("Transfer Successful")

            else:

                print("Insufficient Balance")

        else:

            print("Invalid Account Number")


    # Change PIN

    def change_pin(self):

        acc_no = int(input("Enter Account Number : "))

        account = self.find_account(acc_no)

        if account:

            old_pin = input("Enter Old PIN : ")

            if old_pin == account.pin:

                new_pin = input("Enter New PIN : ")

                account.pin = new_pin

                print("PIN Changed Successfully")

            else:

                print("Wrong PIN")

        else:

            print("Account Not Found")


    # View All Accounts


    def view_all_accounts(self):

        if len(self.accounts) == 0:

            print("No Accounts Available")

        else:

            print("\n====== ALL ACCOUNTS ======")

            for account in self.accounts:

                account.show_details()

                print("-" * 35)

   
    # Delete Account


    def delete_account(self):

        acc_no = int(input("Enter Account Number : "))

        account = self.find_account(acc_no)

        if account:

            self.accounts.remove(account)

            print("Account Deleted Successfully")

        else:

            print("Account Not Found")


    # Total Bank Balance

    def total_bank_balance(self):

        total = 0

        for account in self.accounts:

            total += account.balance

        print("Total Bank Balance :", total)



# Main Program


bank = Bank()

while True:

    print("\n\033[1;91m====== BANKING SYSTEM PRO ======\033[0m")
    print("\033[1;92m1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show Account")
    print("6. Transfer Money")
    print("7. Change PIN")
    print("8. Transaction History")
    print("9. View All Accounts")
    print("10. Delete Account")
    print("11. Total Bank Balance")
    print("12. Exit\033[0m\n")

    choice = input("\033[1;93mEnter Choice : \033[0m")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit_money()

    elif choice == "3":
        bank.withdraw_money()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        bank.show_account()

    elif choice == "6":
        bank.transfer_money()

    elif choice == "7":
        bank.change_pin()

    elif choice == "8":
        bank.history()

    elif choice == "9":
        bank.view_all_accounts()

    elif choice == "10":
        bank.delete_account()

    elif choice == "11":
        bank.total_bank_balance()

    elif choice == "12":
        print("Thank You")
        break

    else:
        print("Invalid Choice")