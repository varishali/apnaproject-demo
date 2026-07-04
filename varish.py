# Correct PIN
correct_pin = "1234"


# Total attempts
attempt = 0


# Maximum attempts
max_attempt = 3


while attempt < max_attempt:


    # User input
    pin = input("Enter ATM PIN : ")


    # Correct PIN
    if pin == correct_pin:


        print("Login Successful")


        break


    # Wrong PIN
    else:


        attempt += 1


        left = max_attempt - attempt


        print(f"Wrong PIN | Attempts Left : {left}")


# Account lock
if attempt == max_attempt:


    print("ATM Card Blocked")