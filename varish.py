total_expense = float(input("Enter Total Expense: "))
people = int(input("Enter Number of People: "))

share = total_expense / people

print("Each Person Pays: ₹", round(share, 2))