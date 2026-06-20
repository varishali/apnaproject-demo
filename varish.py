import random
import time

username = "varish"
password = "1234"

print("==== LOGIN SYSTEM ====")
user = input("Enter Username : ")
passwd = input("Enter Password : ")

if user == username and passwd == password:
    otp = random.randint(1000,9999)

    print(f"Your OTP Is -- {otp} --")
    print("OTP Valid for 20 Seconds!")
    start_time = time.time()
    user_otp = int(input("Enter OTP : "))
    end_time = time.time()
    total_time = end_time - start_time

    if total_time <= 20:
        if user_otp == otp:
            print("Login successful!")

        else:
            print("Invalid OTP!")    

else:
    print("Invalid Username Or Password!")        

