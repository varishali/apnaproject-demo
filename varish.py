# ==========================
# Pet Care Management System
# ==========================

class Pet:

    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age
        self.vaccinated = False

    def show(self):

        print(f"""
Name : {self.name}
Animal : {self.animal}
Age : {self.age}
Vaccinated : {self.vaccinated}
""")


class PetCare:

    def __init__(self):

        self.pets = []

    # Add Pet
    def add_pet(self):

        name = input("Pet Name : ")
        animal = input("Animal Type : ")
        age = int(input("Age : "))

        pet = Pet(name, animal, age)

        self.pets.append(pet)

        print("Pet Added Successfully")

    # View Pets
    def view_pets(self):

        if len(self.pets) == 0:
            print("No Pets Available")
            return

        for pet in self.pets:
            pet.show()

    # Vaccinate Pet
    def vaccinate_pet(self):

        name = input("Pet Name : ")

        for pet in self.pets:

            if pet.name.lower() == name.lower():

                pet.vaccinated = True

                print("Vaccination Updated")

                return

        print("Pet Not Found")

    # Remove Pet
    def remove_pet(self):

        name = input("Pet Name : ")

        for pet in self.pets:

            if pet.name.lower() == name.lower():

                self.pets.remove(pet)

                print("Pet Removed")

                return

        print("Pet Not Found")




care = PetCare()

while True:

    print("\n===== PET CARE MANAGEMENT =====")
    print("1. Add Pet")
    print("2. View Pets")
    print("3. Vaccinate Pet")
    print("4. Remove Pet")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        care.add_pet()

    elif choice == "2":
        care.view_pets()

    elif choice == "3":
        care.vaccinate_pet()

    elif choice == "4":
        care.remove_pet()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")