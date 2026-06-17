saved_username = "varish"
saved_password = "admin123"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == saved_username:

    if password == saved_password:

        print("Login Successful!")

    else:

        print("Wrong Password!")

else:

    print("Username Not Found!")