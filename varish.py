notes = []

while True:

    print("\n===== Notes Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        note = input("Enter Note: ")
        notes.append(note)

        print("Note Added Successfully!")

    elif choice == "2":

        if len(notes) == 0:
            print("No Notes Found!")

        else:

            print("\nYour Notes:")

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "3":

        if len(notes) == 0:
            print("No Notes To Delete!")

        else:

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

            num = int(input("Enter Note Number: "))

            if 1 <= num <= len(notes):
                deleted = notes.pop(num - 1)
                print(f"{deleted} Deleted!")
            else:
                print("Invalid Note Number!")

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")