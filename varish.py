class Book:

    def __init__(self, title):
        self.title = title
        self.issued = False


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, title):

        book = Book(title)
        self.books.append(book)

        print("Book Added Successfully!")

    def view_books(self):

        if len(self.books) == 0:
            print("No Books Available!")

        else:

            print("\nBooks List:")

            for book in self.books:

                status = "Issued" if book.issued else "Available"

                print(f"{book.title} - {status}")

    def issue_book(self, title):

        for book in self.books:

            if book.title == title and not book.issued:

                book.issued = True

                print("Book Issued Successfully!")
                return

        print("Book Not Available!")

    def return_book(self, title):

        for book in self.books:

            if book.title == title and book.issued:

                book.issued = False

                print("Book Returned Successfully!")
                return

        print("Book Not Found!")


library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        title = input("Enter Book Name: ")
        library.add_book(title)

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        title = input("Enter Book Name: ")
        library.issue_book(title)

    elif choice == "4":

        title = input("Enter Book Name: ")
        library.return_book(title)

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")