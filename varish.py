students = {}

while True:

    print("\n===== Attendance System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")

        students[name] = "Absent"

        print("Student Added!")

    elif choice == "2":

        name = input("Enter Student Name: ")

        if name in students:

            status = input("Present/Absent: ")

            students[name] = status

            print("Attendance Updated!")

        else:
            print("Student Not Found!")

    elif choice == "3":

        if len(students) == 0:
            print("No Students Found!")

        else:

            print("\nAttendance Report")

            for name, status in students.items():
                print(f"{name} : {status}")

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")