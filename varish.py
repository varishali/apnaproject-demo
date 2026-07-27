import csv
import os

FILE = "students.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Math", "Science", "English", "Total", "Percent", "Grade"])

def grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 75:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 45:
        return "C"
    else:
        return "Fail"

def add_student():
    name = input("Student Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    total = math + science + english
    percent = round(total / 3, 2)
    g = grade(percent)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, math, science, english, total, percent, g])

    print("Student Record Saved!")

def show_records():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_student():
    name = input("Enter Student Name: ")
    found = False

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0].lower() == name.lower():
                print("\nName      :", row[0])
                print("Math      :", row[1])
                print("Science   :", row[2])
                print("English   :", row[3])
                print("Total     :", row[4])
                print("Percent   :", row[5])
                print("Grade     :", row[6])
                found = True

    if not found:
        print("Student Not Found!")

while True:
    print("\n===== Student Report Card Manager =====")
    print("1. Add Student")
    print("2. Show All Records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_records()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")