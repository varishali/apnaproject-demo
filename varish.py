class Patient:
    def __init__(self, pid, name, age, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease

patients = []
appointments = []

def add_patient():
    pass

def view_patients():
    pass

def search_patient():
    pass

def book_appointment():
    pass

def generate_bill():
    pass

while True:
    print("\n===== Hospital Management System =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Book Appointment")
    print("5. View Appointments")
    print("6. Generate Bill")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        book_appointment()
    elif choice == "5":
        view_appointments()
    elif choice == "6":
        generate_bill()
    elif choice == "7":
        break