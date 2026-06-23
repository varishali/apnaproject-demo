password = "1234"

secret_notes = []

user = input("Enter Password: ")

if user == password:

    while True:

        print("\n1. Add Secret Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            note = input("Write Secret Note: ")

            secret_notes.append(note)

            print("Note Saved!")

        elif choice == "2":

            if len(secret_notes) == 0:

                print("No Notes Found!")

            else:

                for note in secret_notes:

                    print(note)

        elif choice == "3":

            print("Locker Closed!")

            break

        else:

            print("Invalid Choice!")

else:

    print("Wrong Password!")