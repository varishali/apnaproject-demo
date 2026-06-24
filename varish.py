patients = {}


# ADD PATIENT
def add_patient():

    name = input("Enter Patient Name: ")

    disease = input("Enter Disease: ")

    patients[name] = disease

    print("Patient Added Successfully!")


# VIEW PATIENTS
def view_patients():

    if len(patients) == 0:

        print("No Patients Found!")

    else:

        print("\n===== PATIENT RECORDS =====")

        for name, disease in patients.items():

            print("Patient Name:", name)

            print("Disease:", disease)

            print("----------------------")


# SEARCH PATIENT
def search_patient():

    name = input("Enter Patient Name: ")

    if name in patients:

        print("Patient Found!")

        print("Disease:", patients[name])

    else:

        print("Patient Not Found!")


# DELETE PATIENT
def delete_patient():

    name = input("Enter Patient Name To Delete: ")

    if name in patients:

        del patients[name]

        print("Patient Deleted!")

    else:

        print("Patient Not Found!")


# MAIN PROGRAM
while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")


    choice = input("Enter Choice: ")


    if choice == "1":

        add_patient()


    elif choice == "2":

        view_patients()


    elif choice == "3":

        search_patient()


    elif choice == "4":

        delete_patient()


    elif choice == "5":

        print("Program Closed!")

        break


    else:

        print("Invalid Choice!")