users = []

while True:
    print("\n1. Creat Username")
    print("2. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        username = input("Create Username : ")
        if username in users:
            print("Username Alreaady Exists..")
        
        else:
            users.append(username)
            print("Account Created")
        
            print(users)
  
    elif choice == "2":
        print("Program Closed...")
        break
    else:
        print("Invalid Choice!")