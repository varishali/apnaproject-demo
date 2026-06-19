taken_usernames = [
    "varish",
    "admin",
    "python",
    "gaming"
]

username = input("Create Username: ")

if username.lower() in taken_usernames:

    print("Username Already Taken!")

else:

    print("Username Available!")
