class Movie:

    def __init__(self, movie_name, ticket_price):

        self.movie_name = movie_name

        self.ticket_price = ticket_price


class Booking(Movie):

    def __init__(self, movie_name, ticket_price):

        super().__init__(movie_name, ticket_price)

        self.total_tickets = 0

        self.total_amount = 0


    def book_ticket(self):

        tickets = int(input("Enter Number Of Tickets: "))

        self.total_tickets += tickets

        amount = tickets * self.ticket_price

        self.total_amount += amount

        print("Ticket Booked Successfully!")


    def show_details(self):

        print("\n===== BOOKING DETAILS =====")

        print("Movie Name:", self.movie_name)

        print("Ticket Price:", self.ticket_price)

        print("Total Tickets:", self.total_tickets)

        print("Total Amount:", self.total_amount)


movie1 = Booking("Pushpa 3", 250)


while True:

    print("\n===== MOVIE TICKET SYSTEM =====")

    print("1. Book Ticket")

    print("2. Show Details")

    print("3. Exit")


    choice = input("Enter Choice: ")


    if choice == "1":

        movie1.book_ticket()


    elif choice == "2":

        movie1.show_details()


    elif choice == "3":

        print("Thank You!")

        break


    else:

        print("Invalid Choice!")