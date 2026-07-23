import pandas as pd
import os

FILE = "employees.csv"

# Create CSV if it doesn't exist
if not os.path.exists(FILE):
    data = {
        "ID": [101, 102, 103, 104, 105],
        "Name": ["Aman", "Rahul", "Neha", "Priya", "Rohan"],
        "Department": ["IT", "HR", "IT", "Sales", "HR"],
        "Salary": [45000, 38000, 52000, 41000, 36000]
    }
    pd.DataFrame(data).to_csv(FILE, index=False)

# Read data
df = pd.read_csv(FILE)

print("\n===== EMPLOYEE DATA =====")
print(df)

print("\nHighest Salary:")
print(df.loc[df["Salary"].idxmax()])

print("\nLowest Salary:")
print(df.loc[df["Salary"].idxmin()])

print("\nAverage Salary:", df["Salary"].mean())

print("\nDepartment Wise Salary")
print(df.groupby("Department")["Salary"].mean())

# Bonus (10%)
df["Bonus"] = df["Salary"] * 0.10
df["Total Salary"] = df["Salary"] + df["Bonus"]

df.to_csv("employee_salary_report.csv", index=False)

print("\nReport saved as employee_salary_report.csv")