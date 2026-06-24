books = {}


# ADD BOOK
def add_book():

    name = input("Enter Book Name: ")

    author = input("Enter Author Name: ")

    books[name] = author

    print("Book Added Successfully!")


# VIEW BOOKS
def view_books():

    if len(books) == 0:

        print("No Books Available!")

    else:

        print("\n===== BOOK LIST =====")

        for book, author in books.items():

            print("Book:", book)

            print("Author:", author)

            print("-------------------")


# SEARCH BOOK
def search_book():

    name = input("Enter Book Name: ")

    if name in books:

        print("Book Found!")

        print("Author:", books[name])

    else:

        print("Book Not Found!")


# DELETE BOOK
def delete_book():

    name = input("Enter Book Name To Delete: ")

    if name in books:

        del books[name]

        print("Book Deleted!")

    else:

        print("Book Not Found!")


# MAIN PROGRAM
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")


    choice = input("Enter Choice: ")


    if choice == "1":

        add_book()


    elif choice == "2":

        view_books()


    elif choice == "3":

        search_book()


    elif choice == "4":

        delete_book()


    elif choice == "5":

        print("Program Closed!")

        break


    else:

        print("Invalid Choice!")