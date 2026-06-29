password = input("Enter Password : ")

if len(password) >= 8:

    if any(char.isdigit() for char in password):

        print("Strong Password")

    else:

        print("Add Numbers")

else:

    print("Weak Password")