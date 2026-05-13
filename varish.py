class Account:
    print("----------------------")
    print("\033[1mWELCOME TO VARISH BANK\033[0m")
    print("----------------------")
    def __init__(self,bal,acc,password):
        self.balance = bal
        self.account_number = acc
        self.password = password

    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance.")

        else:    
            self.balance -= amount
            print("RS.",amount,"was debited.")
            print("total balance is",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("RS.",amount,"was credited.")
        print("total balance is ",self.get_balance())

    def get_balance(self):
        return self.balance
        
acc1 = Account(15000,1234567890,"12345")

password = input("enter your password to continue : ")


if password == acc1.password:
    print("--- \033[1mlogin succesful\033[0m ---")
    print("current balance :",acc1.get_balance())


    options = int(input("Enter (1) for credit and (2) for debit :"))

    if options == 1:
        print("you have selected credit option :")
        input1 = int(input("Enter the amount to credit: ") )
        acc1.credit(input1)

    elif options == 2:     
        print("you have selected debit option :")
        input1 = int(input("enter the amount to debit: "))
        acc1.debit(input1) 
    else:
        print("Invalid options!")      

else:
    print("Invalid password!")
    print("Please try again")         










      
    




   

        
