taken_usernames = [
    "admin",
    "varish",
    "python",
    "user123"
]

username = input("Enter Username: ")

if username.lower() in taken_usernames:

    print("Username Already Taken!")

else:

    print("Username Available!")