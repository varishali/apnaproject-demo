users = {}

while True :
    print("\n\033[1;92m==== LOGIN SYSTEM ====\033[0m")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your Choice : ")

    #signup
    if choice == "1":
        username = input("Creat username : ")
        if username in users:
            print("Username Already Exists! ")

        else:
            password = input("Creat password : ")
            users[username] = password
            print("Account Created Successfully!")

    elif choice == "2":
        username = input("Enter Username : ")
        if username in users:

            attempts = 3

            while attempts > 0 :
                password = input("Enter Password : ")

                if users[username] == password:
                    print("login Successfully!")
                    break
                else:
                    attempts -= 1
                    print("Wrong Password!")
                    print("Attempts Left : ",attempts)

            if attempts == 0:
                print("Account Temporaily Locked!")
                break
           

    elif choice == "3":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")                        