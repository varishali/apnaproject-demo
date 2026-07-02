import random

chars = "abcd1234XYZ"

password = ""

for i in range(6):

    password += random.choice(chars)

print("Password :", password)