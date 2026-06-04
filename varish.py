students = {}

while True:

    print("\n===== Student Report Card =====")
    print("1. Add Student")
    print("2. View Report")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Student Name: ")

        marks = []

        for i in range(3):
            mark = float(input(f"Enter Subject {i+1} Marks: "))
            marks.append(mark)

        students[name] = marks

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found!")

        else:

            for name, marks in students.items():

                average = sum(marks) / len(marks)

                if average >= 90:
                    grade = "A"
                elif average >= 75:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                else:
                    grade = "D"

                print("\nName:", name)
                print("Marks:", marks)
                print("Average:", round(average, 2))
                print("Grade:", grade)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")