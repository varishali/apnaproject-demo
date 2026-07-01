class Employee:

    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id 
        self.salary = salary

    def show_details(self):
        print("== EMPLOYEE DETAILS ==")
        print(f"Employee Name : {self.name}")
        print(f"Emplyee ID : {self.emp_id}")
        print(f"Employee Salary : {self.salary}")

class Management:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter Employee Name : ")
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Employee Salary : "))
        emp = Employee(name, emp_id, salary)
        self.employees.append(emp)
        print("Employee Added Successfully!")

    def show_all_employees(self):
        if len(self.employees) == 0:
            print("No Employees Found!")

        else:
            for emp in self.employees:
                emp.show_details()

    def search_employees(self):
        search_id = input("Enter Employee ID to search : ")
        found = False

        for emp in self.employees:

            if emp.emp_id == search_id:
                emp.show_details()

                found = True
                
        if found == False:
            print("Employee Not Found!")

    def delete_employee(self):

        delete_id = input("Enter Employee ID to delete : ")
        for emp in self.employees:
            if emp.emp_id == delete_id:
                self.employees.remove(emp)
                print("Employee Delete Successfully!")
                return
            
        print("Employee Not Found! ")

system = Management()

while True:
    print("\n=====  EMPLOYEE MANAGEMENT SYSTEM  =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Delete Employee ")
    print("5. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        system.add_employee()

    elif choice == "2":
        system.show_all_employees()

    elif choice == "3":
        system.search_employees()

    elif choice == "4":
        system.delete_employee()

    elif choice == "5":
        print("Exiting the Program...")
        break 
    else:
        print("Invalid choice please try again!")                 