# ==========================
# Bicycle Rental System
# ==========================

class Bicycle:

    def __init__(self, bike_no):
        self.bike_no = bike_no
        self.available = True


class Rental:

    def __init__(self):
        self.bikes = []

    # Add Bicycle
    def add_bike(self):

        bike_no = input("Bike Number : ")

        bike = Bicycle(bike_no)

        self.bikes.append(bike)

        print("Bike Added")

    # View Bikes
    def view_bikes(self):

        if len(self.bikes) == 0:
            print("No Bikes Available")
            return

        print("\n===== Bicycle List =====")

        for bike in self.bikes:

            print(
                f"Bike : {bike.bike_no} | Available : {bike.available}"
            )

    # Rent Bicycle
    def rent_bike(self):

        bike_no = input("Bike Number : ")

        for bike in self.bikes:

            if bike.bike_no == bike_no:

                if bike.available:

                    bike.available = False

                    print("Bike Rented Successfully")

                else:

                    print("Bike Already Rented")

                return

        print("Bike Not Found")

    # Return Bicycle
    def return_bike(self):

        bike_no = input("Bike Number : ")

        for bike in self.bikes:

            if bike.bike_no == bike_no:

                if not bike.available:

                    bike.available = True

                    print("Bike Returned")

                else:

                    print("Bike Already Available")

                return

        print("Bike Not Found")


# ==========================
# Main Program
# ==========================

rental = Rental()

while True:

    print("\n===== Bicycle Rental =====")

    print("1. Add Bicycle")
    print("2. View Bicycles")
    print("3. Rent Bicycle")
    print("4. Return Bicycle")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        rental.add_bike()

    elif choice == "2":
        rental.view_bikes()

    elif choice == "3":
        rental.rent_bike()

    elif choice == "4":
        rental.return_bike()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
