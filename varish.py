books = []

while True:
    print("\n===== LIBRARY BOOK MANAGER =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book Added Successfully!")

    elif choice == "2":
        if books:
            print("\nAvailable Books:")
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")
        else:
            print("No Books Available.")

    elif choice == "3":
        search = input("Enter Book Name: ")
        if search in books:
            print("Book Found!")
        else:
            print("Book Not Found.")

    elif choice == "4":
        remove = input("Enter Book Name: ")
        if remove in books:
            books.remove(remove)
            print("Book Removed Successfully!")
        else:
            print("Book Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")