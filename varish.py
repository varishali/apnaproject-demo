import pandas as pd


class StudentManager:

    def __init__(self):
        try:
            self.df = pd.read_csv("students.csv")
            print("Data Loaded Successfully!\n")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["ID", "Name", "Marks"])
            print("New Student Database Created!\n")

    def add_student(self):
        student_id = int(input("Enter ID : "))
        name = input("Enter Name : ")
        marks = float(input("Enter Marks : "))

        new_student = pd.DataFrame({
            "ID": [student_id],
            "Name": [name],
            "Marks": [marks]
        })

        self.df = pd.concat([self.df, new_student], ignore_index=True)
        print("Student Added Successfully!\n")

    def view_students(self):
        if self.df.empty:
            print("No Students Found.\n")
        else:
            print(self.df)

    def search_student(self):
        student_id = int(input("Enter Student ID : "))
        student = self.df[self.df["ID"] == student_id]

        if student.empty:
            print("Student Not Found.\n")
        else:
            print(student)

    def result_analysis(self):
        if self.df.empty:
            print("No Data Available.\n")
            return

        print("\n----- Result Analysis -----")
        print("Highest Marks :", self.df["Marks"].max())
        print("Lowest Marks  :", self.df["Marks"].min())
        print("Average Marks :", round(self.df["Marks"].mean(), 2))

    def save_data(self):
        self.df.to_csv("students.csv", index=False)
        print("Data Saved Successfully!\n")


manager = StudentManager()

while True:
    print("\n===== Student Result Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Result Analysis")
    print("5. Save Data")
    print("6. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.result_analysis()

    elif choice == "5":
        manager.save_data()

    elif choice == "6":
        manager.save_data()
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

