# password generator

import random
import string

print("welcome to password generator")

length = int(input("enter password length: "))

letters = string.ascii_letters
digit = string.digits
symbols = string.punctuation

all_characters = letters + digit + symbols

password = " " 

for i in range(length):
    password += random.choice(all_characters)

print("your password is:" + password)



    













