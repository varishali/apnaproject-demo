balance = 5000

upi_pin = "1234"

amount = int(input("Enter Amount: "))

pin = input("Enter UPI PIN: ")

if pin == upi_pin:

    if amount <= balance:

        balance -= amount

        print("Payment Successful!")

        print("Remaining Balance:", balance)

    else:

        print("Insufficient Balance!")

else:

    print("Wrong UPI PIN!")