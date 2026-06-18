balance = 5000

amount = int(input("Enter Purchase Amount: "))

if amount <= balance:

    balance -= amount

    print("Payment Successful!")
    print("Remaining Balance:", balance)

else:

    print("Insufficient Balance!")