import pandas as pd

username = "admin"
password = "1234"

user = input("\033[0;96mEnter Username : \033[0m")
passwd = input("\033[0;96mEnter Password : \033[0m")

if user == username and passwd == password:
    print("\033[0;97mLogin Successfully !\033[0m")
else:
    print("Wrong Username Or password !")    
    exit()


students = {}

# add student
def add_student():
    name = input("\033[0;96mEnter Student Name : \033[0m")
    marks = int(input("\033[0;96mEnter Marks : \033[0m"))
    students[name] = marks
    print("Student Added Successfully!")

# view students
def view_student():
    if len(students) == 0:
        print("No Students Found..")
    else:
        data = {
            "Name":list(students.keys()),
            "Marks":list(students.values())
        }
        df = pd.DataFrame(data)
        print("\n\033[1:93m==== STUDENT RECORDS ====\033[0m")
        print(df)

# search students
def search_student():
    name = input("Enter Students Name To Search : ")
    if name in students:
        print(name,"Marks : ",students[name])
    else:
        print("Student Not Found..")

# delete student
def delete_student():
    name = input("Enter Students Name To Delete : ")

    if name in students:
        del students[name]
        print("Student Delete..")
    else:
        print("Student Not Found..")


# main program 
while True:
    print("\n\033[1;92m===== STUDENT MANAGEMENT SYSTEM =====\033[0m") 
    print("\033[1;94m1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit\033[0m")

    choice = input("\n\033[1;95mEnter Choice : \033[0m")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_student()   

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()                    

    elif choice == "5":
        print("Program Closed ..")
        break
    else:
        print("Invalid Choice!")