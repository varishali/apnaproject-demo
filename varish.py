tickets = []

total_seats = 5

while True:

    print("\n===== TRAIN TICKET BOOKING SYSTEM =====")
    print("1. Book Ticket")
    print("2. View Passengers")
    print("3. Cancel Ticket")
    print("4. Available Seats")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        if len(tickets) >= total_seats:
            print("No Seats Available!")

        else:

            name = input("Enter Passenger Name: ")
            age = int(input("Enter Age: "))

            seat_no = len(tickets) + 1

            tickets.append({
                "name": name,
                "age": age,
                "seat": seat_no
            })

            print(f"Ticket Booked Successfully!")
            print(f"Seat Number: {seat_no}")

    elif choice == "2":

        if len(tickets) == 0:
            print("No Bookings Found!")

        else:

            print("\n===== PASSENGER LIST =====")

            for passenger in tickets:

                print(
                    f"Name: {passenger['name']} | "
                    f"Age: {passenger['age']} | "
                    f"Seat: {passenger['seat']}"
                )

    elif choice == "3":

        name = input("Enter Passenger Name: ")

        found = False

        for passenger in tickets:

            if passenger["name"].lower() == name.lower():

                tickets.remove(passenger)

                found = True

                print("Ticket Cancelled Successfully!")
                break

        if not found:
            print("Passenger Not Found!")

    elif choice == "4":

        available = total_seats - len(tickets)

        print("Available Seats:", available)

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")