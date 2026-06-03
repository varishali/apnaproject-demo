import pandas as pd
from datetime import datetime

expenses = []

while True:
    print("\n\033[1;92m=== Expense Tracker App ===\033[0m")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("\033[1;94mEnter Your Choice : \033[0m")
    if choice == "1":
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        category = input("Enter Category (Food,Travel,Shopping): ")
        try:
            amount = float(input("Enter Amount : "))
        except ValueError:
            print("Please Enter A Valid Number for Amount.")
            continue
        expenses.append([current_time,category,amount])
        print(f"\033[1;93m{category} Expense of ${amount} added successfully.\033[0m")

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expensed Added Yet.")
        else:
            df = pd.DataFrame(expenses, columns=["current_time","Category","Amount"])    
            print("\n\033[1;93mYour Expenses : \033[0m")
            print(df)
            

    elif choice == "3":
        if len(expenses) == 0:
            print("No Expenses Added Yet.")

        else:
            df = pd.DataFrame(expenses,columns=["current_time","Category","Amount"])
            print("\n\033[1;93mTotal Expenses $: \033[0m",df["Amount"].sum())
            print("\n\033[1;93mHighest Expense $: \033[0m",df["Amount"].max())
            print("\n\033[1;93mLowest Expense $: \033[0m",df["Amount"].min())
            print("\n\033[1;93mTotal Record $: \033[0m",len(df))
            print("\n\033[1;93mLowest Expense $: \033[0m",df["Amount"].min())

   

    elif choice == "4":
        print("\nThanks For Using This App")
        break         
    else:
        print("\nInvalid Choice.")