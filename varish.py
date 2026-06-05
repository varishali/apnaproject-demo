password = input("Enter Password: ")

if len(password) < 6:
    print("Weak Password")

elif len(password) < 10:
    print("Medium Password")

else:
    print("Strong Password")