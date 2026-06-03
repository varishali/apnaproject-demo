contacts = {}

while True:

    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone

        print("Contact Added Successfully!")

    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts Found!")

        else:
            print("\nContacts List:")

            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":

        name = input("Enter Name To Search: ")

        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact Not Found!")

    elif choice == "4":

        name = input("Enter Name To Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":

        print("Thanks For Using Contact Book!")
        break

    else:

        print("Invalid Choice!")
