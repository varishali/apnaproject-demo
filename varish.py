import csv
import os

FILE = "expenses.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount"])

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([category, amount])

    print("Expense Added Successfully!")

def view_expenses():
    total = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        print("\nCategory\tAmount")

        for row in reader:
            print(f"{row[0]}\t\t₹{row[1]}")
            total += float(row[1])

    print("-" * 30)
    print("Total Expense = ₹", total)

def search_category():
    category = input("Enter Category: ")

    found = False

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0].lower() == category.lower():
                print(row)
                found = True

    if not found:
        print("No Record Found!")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Category")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")