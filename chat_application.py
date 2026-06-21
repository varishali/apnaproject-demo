users = {
    "varish" : "1234",
    "ali" : "0123"
}

chat_history = []

# login
def login():
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username in users and users[username] == password:
        print("Login successful..")
        chat_system(username)
    else:
        print("Wrong Username Or password..")    

# chat system
def chat_system(username):

    while True:
        print("======  CHAT MENU  ======")

        print("1. Send Message")
        print("2. View Chat")
        print("3. Logout")

        choice = input("Enter Choice : ")

        # send message
        if choice == "1":
            message = input("Enter Message : ")
            chat_history.append(
                f"{username}: {message}")

            print("Message Sent!")

        elif choice == "2":
            print("====  Chat History  ====")

            if len(chat_history) == 0:
                print("No Message !")
            else:
                for msg in chat_history:
                    print(msg)

        elif choice == "3":
            print("Logged Out!")

            break
        else:
            print("Invalid Choice!")

# main program
while True :
    print("\n====  CHAT APPLICATION  ====")

    print("1. Login")
    print("2. Exit")

    choice = input("Enter Choice : ")
    if choice == "1":
        login()

    elif choice == "2":
        print("Program Closed ..")

        break
    else:
        print("Invalid Choice ..")  