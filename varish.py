password = input("Enter Password : ")

upper = False
lower = False
digit = False
special = False


for ch in password:

    if ch.isupper():

        upper = True

    elif ch.islower():

        lower = True

    elif ch.isdigit():

        digit = True

    else:

        special = True


if upper and lower and digit and special:

    print("Strong Password")

else:

    print("Weak Password")

