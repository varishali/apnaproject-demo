import random

otp = random.randint(1000,9999)

print("OTP : ",otp)

user_otp = int(input("Enter OTP : "))

if user_otp == otp:
    print("Verified..")

else:
    print("Wrong OTP..")    


