class Room:
    def __init__(self,room_no,price):
        self.room_no = room_no
        self.price = price
        self.booked = False

    def show_room(self):
        print(f"Room Number : {self.room_no}, Price : {self.price}, Booking Status : {self.booked}")   

class Customer:
    def __init__(self,name,age,room):

        self.name = name
        self.age = age
        self.room = room

    def show_customer(self):
        print(f"Costumer Name : {self.name}, Age : {self.age}, Room Number : {self.room.room_no}, Room Price : {self.room.price}, Booking Status : {self.room.booked}")

    
class Hotel:
    def __init__(self):

        # room list
        self.rooms = []

        # customer list
        self.customers = []

    # add rooms
    def add_room(self):
        room_no = input("Enter Room Number : ")
        price = int(input("Enter Room Price : "))

        # room object create
        room = Room(room_no,price)
        self.rooms.append(room)
        print("Room Added")

    # view all rooms
    def view_room(self):
        if len(self.rooms) == 0:
            print("No Rooms Available")
        else:
            for room in self.rooms:
                room.show_room()

    # book rooms
    def book_room(self):
        room_no = input("Enter Room Number : ")
        customer_name = input("Enter Customer Name : ")
        customer_age = input("Enter Customer Age : ")

        # search room
        for room in self.rooms:

            # roo available
            if room.room_no == room_no and room.booked == False:

                room.booked = True

                customer = Customer(customer_name,customer_age,room)

                # save customer
                self.customers.append(customer)
                print("Room Booked")
                return
        print("Room Not Available")


    def view_customer(self):
        if len(self.customers) == 0 :
            print("No Customer Available")
        else:
            for customer in self.customers:
                customer.show_customer()

    def total_revenue(self):
        total = 0 

        for customer in self.customers:
            total += customer.room.price
        print("Total Revenue : ",total)


# object create
hotel = Hotel()                      

# main program
while True:
    print("\n====  DERKVR HOTEL MANAGEMENT  ====")
    print("1. Add Room")
    print("2. View Room")
    print("3. Book Room")
    print("4. View Customer")
    print("5. Total Revenue")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        hotel.add_room()

    elif choice == "2":
        hotel.view_room()

    elif choice == "3":
        hotel.book_room()

    elif choice == "4":
        hotel.view_customer()

    elif choice == "5":
        hotel.total_revenue()

    elif choice == "6":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")
