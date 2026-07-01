class Library:

    def __init__(self):
        self.books = {}

    def add_book(self):

        name = input("Enter the name of the book : ")
        author = input("Enter the name of the author : ")

        if name in self.books:
            print("book already axixts in library.")
        else:
            self.books[name] = author
            print("Book added successfully.")    

    def view_books(self):

        if not self.books:
            print("No books available in the library.")
        else:
            print("books available in library : ")

            for name,author in self.books.items():
                print(f"Book Name : {name}, author : {author}")

    def search_book(self):
        name = input("Enter the name of the book to search : ")
        if name in self.books:
            print(f"Book found ! Book name : {name}, author : {self.books[name]}")
        else:
            print("Book not found in the library.")

    def delete_book(self):
        name = input("Enter tth name of the book to delete : ")
        if name in self.books:
            del self.boos[name]
            print("Book delete Successfully.")

        else :
            print("Book not found in the library.")

library = Library()

while True :
    print("\n=====  SMART LIBRARY MANAGRMENT SYSTEM  =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book ")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1 - 5) : ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.delete_book()            

    elif choice == "5":
        print("Exiting th eprogram.")
        break
    else:
        print("Invalid choice. Plaese enter a valid option (1 - 5) ")



