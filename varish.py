import pandas as pd
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
        df.to_csv(FILE_NAME, index=False)


def load_data():
    return pd.read_csv(FILE_NAME)


def save_data(df):
    df.to_csv(FILE_NAME, index=False)


def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    df = load_data()

    new_data = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount],
        "Description": [description]
    })

    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df)

    print("\nExpense Added Successfully!\n")


def view_expenses():
    df = load_data()

    if df.empty:
        print("\nNo Expense Found.\n")
    else:
        print("\n===== ALL EXPENSES =====")
        print(df.to_string(index=False))


def search_category():
    df = load_data()

    cat = input("Enter Category: ")

    result = df[df["Category"].str.lower() == cat.lower()]

    if result.empty:
        print("\nNo Record Found.\n")
    else:
        print(result.to_string(index=False))


def total_expense():
    df = load_data()

    total = df["Amount"].sum()

    print(f"\nTotal Expense = ₹{total:.2f}\n")


def delete_expense():
    df = load_data()

    if df.empty:
        print("No Data Available.")
        return

    print(df)

    index = int(input("\nEnter Row Number To Delete: "))

    if index in df.index:
        df = df.drop(index)
        df.reset_index(drop=True, inplace=True)
        save_data(df)
        print("Expense Deleted Successfully.")
    else:
        print("Invalid Row Number.")


def monthly_summary():
    df = load_data()

    if df.empty:
        print("No Data Available.")
        return

    df["Date"] = pd.to_datetime(df["Date"])

    df["Month"] = df["Date"].dt.strftime("%B")

    summary = df.groupby("Month")["Amount"].sum()

    print("\n===== MONTHLY SUMMARY =====")
    print(summary)


def highest_expense():
    df = load_data()

    if df.empty:
        print("No Data Available.")
        return

    high = df.loc[df["Amount"].idxmax()]

    print("\nHighest Expense")
    print(high)


def menu():
    while True:
        print("""
========== SMART EXPENSE TRACKER ==========
1. Add Expense
2. View Expenses
3. Search Category
4. Total Expense
5. Monthly Summary
6. Highest Expense
7. Delete Expense
8. Exit
===========================================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_category()

        elif choice == "4":
            total_expense()

        elif choice == "5":
            monthly_summary()

        elif choice == "6":
            highest_expense()

        elif choice == "7":
            delete_expense()

        elif choice == "8":
            print("\nThank You For Using Expense Tracker!")
            break

        else:
            print("\nInvalid Choice.\n")


create_file()
menu()