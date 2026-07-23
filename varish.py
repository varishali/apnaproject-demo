import pandas as pd
import os

FILE = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        date = input("Date (DD-MM-YYYY): ")
        category = input("Category: ")
        amount = float(input("Amount: "))

        df = pd.read_csv(FILE)

        new = pd.DataFrame({
            "Date": [date],
            "Category": [category],
            "Amount": [amount]
        })

        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(FILE, index=False)

        print("Expense Added Successfully!")

    elif choice == "2":
        df = pd.read_csv(FILE)

        if df.empty:
            print("No Expenses Found!")
        else:
            print(df)

    elif choice == "3":
        df = pd.read_csv(FILE)

        print("\nTotal Expense:", df["Amount"].sum())

        print("\nCategory Wise Expense")
        print(df.groupby("Category")["Amount"].sum())

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")