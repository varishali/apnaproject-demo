class Room:

    def __init__(self, room_no):
        self.room_no = room_no
        self.booked = False


class Hotel:

    def __init__(self):
        self.rooms = []

        for i in range(101, 106):
            self.rooms.append(Room(i))

    def view_rooms(self):

        print("\nRoom Status:")

        for room in self.rooms:

            status = "Booked" if room.booked else "Available"

            print(f"Room {room.room_no} - {status}")

    def book_room(self, room_no):

        for room in self.rooms:

            if room.room_no == room_no:

                if not room.booked:

                    room.booked = True
                    print("Room Booked Successfully!")

                else:
                    print("Room Already Booked!")

                return

        print("Room Not Found!")

    def cancel_booking(self, room_no):

        for room in self.rooms:

            if room.room_no == room_no:

                if room.booked:

                    room.booked = False
                    print("Booking Cancelled!")

                else:
                    print("Room Already Available!")

                return

        print("Room Not Found!")


hotel = Hotel()

while True:

    print("\n===== HOTEL BOOKING SYSTEM =====")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        hotel.view_rooms()

    elif choice == "2":

        room_no = int(input("Enter Room Number: "))
        hotel.book_room(room_no)

    elif choice == "3":

        room_no = int(input("Enter Room Number: "))
        hotel.cancel_booking(room_no)

    elif choice == "4":

        break

    else:

        print("Invalid Choice!")