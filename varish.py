students = {}


# ADD STUDENT
def add_student():

    name = input("Enter Student Name : ")

    marks = int(input("Enter Marks : "))

    students[name] = marks

    print("Student Added Successfully!")


# VIEW RESULT
def view_result():

    if len(students) == 0:

        print("No Student Found!")

    else:

        print("\n===== STUDENT RESULTS =====")

        for name, marks in students.items():

            print("\nName :", name)

            print("Marks :", marks)


            if marks >= 90:

                print("Grade : A")

            elif marks >= 70:

                print("Grade : B")

            elif marks >= 50:

                print("Grade : C")

            else:

                print("Fail")


# TOPPER
def topper():

    if len(students) == 0:

        print("No Student Found!")

    else:

        top_student = max(students, key=students.get)

        print("Topper :", top_student)

        print("Marks :", students[top_student])


# MAIN PROGRAM
while True:

    print("\n===== STUDENT RESULT SYSTEM =====")

    print("1. Add Student")

    print("2. View Results")

    print("3. Show Topper")

    print("4. Exit")


    choice = input("Enter Choice : ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_result()


    elif choice == "3":

        topper()


    elif choice == "4":

        print("Program Closed!")

        break


    else:

        print("Invalid Choice!")