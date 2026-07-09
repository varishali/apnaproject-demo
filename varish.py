class Movie:

    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats

    def show(self):
        print(f"{self.name} | Price: ₹{self.price} | Seats: {self.seats}")


class BookingSystem:

    def __init__(self):
        self.movies = []

 
    def add_movie(self):

        name = input("Movie Name : ")
        price = int(input("Ticket Price : "))
        seats = int(input("Total Seats : "))

        movie = Movie(name, price, seats)

        self.movies.append(movie)

        print("Movie Added Successfully")

    def view_movies(self):

        if len(self.movies) == 0:
            print("No Movies Available")
            return

        print("\n===== Movies =====")

        for movie in self.movies:
            movie.show()

    def book_ticket(self):

        name = input("Movie Name : ")

        for movie in self.movies:

            if movie.name.lower() == name.lower():

                tickets = int(input("How Many Tickets : "))

                if tickets <= movie.seats:

                    movie.seats -= tickets

                    bill = tickets * movie.price

                    print("Booking Successful")
                    print("Total Bill :", bill)

                else:

                    print("Seats Not Available")

                return

        print("Movie Not Found")

    def search_movie(self):

        name = input("Enter Movie Name : ")

        for movie in self.movies:

            if movie.name.lower() == name.lower():

                movie.show()
                return

        print("Movie Not Found")

    def delete_movie(self):

        name = input("Movie Name : ")

        for movie in self.movies:

            if movie.name.lower() == name.lower():

                self.movies.remove(movie)

                print("Movie Deleted")

                return

        print("Movie Not Found")


system = BookingSystem()



while True:

    print("\n====== Movie Ticket Booking ======")

    print("1. Add Movie")
    print("2. View Movies")
    print("3. Book Ticket")
    print("4. Search Movie")
    print("5. Delete Movie")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        system.add_movie()

    elif choice == "2":

        system.view_movies()

    elif choice == "3":

        system.book_ticket()

    elif choice == "4":

        system.search_movie()

    elif choice == "5":

        system.delete_movie()

    elif choice == "6":

        print("Program Closed")

        break

    else:

        print("Invalid Choice")