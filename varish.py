import pandas as pd
books = {}

# add book
def add_book():
    name = input("\nEnter Book Name : ")
    author = input("Enter Author Name : ")
    books[name] = author
    print("Book Added Successfully.")

# view book 
def view_book():
    if len(books) == 0:
        print("No Books Found.")
    else:
        data = {
            "Book Name" : list(books.keys()),
            "Author Name" : list(books.values()) 
        }
        df = pd.DataFrame(data)
        print("\n",df,"\n")

    
# search book 
def search_book():
    name = input("Enter Book Name : ")
    if name in books :
        print("Book Found : ",books)
        print("Author : ",books[name])

    else:
        print("No book Found.")

# delete book
def delete_book():
    name = input("Enter Book Name TO Delete : ")
    if name in books:
        del books[name]
        print("Book Dlete.")
    else:
        print("No Books Found.")

# main program 
while True:
    print("\n====  LIBRARY MANAGEMENT SYSTEM  ====\n")
    print("1. Add Book")
    print("2. View Book")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit\n")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_book()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book() 

    elif choice == "5":
        print("Program Closed.")
        break 
    else:
        print("Invalid Choice")      
             

