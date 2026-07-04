# Total parking slots
slots = 5


# Parked vehicles
parked = []


while True:


    print("\n===== PARKING SYSTEM =====")


    print("Available Slots :", slots)


    print("1. Park Vehicle")

    print("2. Remove Vehicle")

    print("3. View Parked Vehicles")

    print("4. Exit")


    choice = input("Enter Choice : ")


    if choice == "1":


        if slots > 0:


            vehicle = input("Enter Vehicle Number : ")


            parked.append(vehicle)


            slots -= 1


            print("Vehicle Parked ")


        else:


            print("Parking Full ")


    elif choice == "2":


        vehicle = input("Enter Vehicle Number : ")


        if vehicle in parked:


            parked.remove(vehicle)


            slots += 1


            print("Vehicle Removed")


        else:


            print("Vehicle Not Found")


    elif choice == "3":


        print("\nParked Vehicles :")


        if len(parked) == 0:


            print("No Vehicles")


        else:


            for vehicle in parked:


                print(vehicle)

    elif choice == "4":


        print("Program Closed")


        break

    else:


        print("Invalid Choice")