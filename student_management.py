print("\033[1m=== STUDENT MANAGEMENT SYSTEM ===\033[0m")

password = "admin1234"

user_password = input("Enter password : ")
if user_password == password:
    print("\033[1m== Login Successful! ==\033[0m")

    students = {
    "varish" : 90,
    "rahul" : 89,
    "aman" : 78

}

while True:
    print("\033[1m== MENU ==\033[0m")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter Student Name : ")
        marks = int(input("Enter marks : "))
        students[name] = marks
        print("Student Added Successfully.")

        again = input("Do you want to contine ?(yes / no) : ")
        if again == "no":
            print("Program Closed")
            break 

    elif choice == "2":
        print("Student Records : ")
        for name,marks in students.items():
            print(name,":",marks)

        again = input("Do you want to contine ?(yes / no) : ")
        if again == "no":
            print("Program Closed")
            break    


    elif choice == "3":
        search = input("Enter Student Name : ")
        if search in students:  
            print(search,"marks",students[search]) 

        else:
            print("Student not found !")

        again = input("Do you want to contine ?(yes / no) : ")
        if again == "no":
            print("Program Closed")
            break    

    elif choice == "4":
        delete = input("Enter Student Name : ")
        if delete in students:
            del students[delete]
            print("Student deleted !")
        else:
            print("student not found !")

        again = input("Do you want to contine ?(yes / no) : ")
        if again == "no":
            print("Program Closed")
            break    

    elif choice == "5":
        print("Program closed !")

        break
    else:
        print("Invalid choice ! ")              







                 
    
