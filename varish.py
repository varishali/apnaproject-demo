import pandas as pd
import numpy as np

# -----------------------------
# Sample Data
# -----------------------------
data = {
    "Emp_ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Aman","Riya","Ali","Sneha","Rohit",
             "Priya","Karan","Neha","Arjun","Sara"],
    "Department": ["IT","HR","IT","Finance","HR",
                   "IT","Finance","HR","IT","Finance"],
    "Salary": [50000,42000,65000,70000,45000,
               60000,72000,43000,68000,75000],
    "Experience": [2,1,5,7,3,4,8,2,6,9],
    "Performance": [88,75,92,95,70,90,98,80,94,99]
}

df = pd.DataFrame(data)

# -----------------------------
# Missing Values Check
# -----------------------------
print("\nMissing Values\n")
print(df.isnull().sum())

# -----------------------------
# Bonus Calculation
# -----------------------------
df["Bonus"] = np.where(df["Performance"] >= 90,
                       df["Salary"] * 0.20,
                       df["Salary"] * 0.10)

# -----------------------------
# Total Salary
# -----------------------------
df["Total Salary"] = df["Salary"] + df["Bonus"]

# -----------------------------
# Performance Grade
# -----------------------------
conditions = [
    df["Performance"] >= 90,
    df["Performance"] >= 80,
    df["Performance"] >= 70
]

grades = ["A", "B", "C"]

df["Grade"] = np.select(conditions, grades, default="D")

# -----------------------------
# Department Summary
# -----------------------------
summary = df.groupby("Department").agg({
    "Salary":"mean",
    "Performance":"mean",
    "Bonus":"sum"
})

print("\nDepartment Summary\n")
print(summary)

# -----------------------------
# Top 5 Employees
# -----------------------------
top5 = df.sort_values("Performance", ascending=False).head(5)

print("\nTop Performers\n")
print(top5[["Name","Performance","Grade"]])

# -----------------------------
# Highest Salary
# -----------------------------
highest = df.loc[df["Salary"].idxmax()]

print("\nHighest Salary Employee\n")
print(highest)

# -----------------------------
# Pivot Table
# -----------------------------
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Grade",
    aggfunc="mean",
    fill_value=0
)

print("\nPivot Table\n")
print(pivot)

# -----------------------------
# Statistics
# -----------------------------
print("\nStatistics\n")
print(df.describe())

# -----------------------------
# Save Files
# -----------------------------
df.to_csv("employee_report.csv", index=False)
summary.to_csv("department_summary.csv")
pivot.to_csv("salary_pivot.csv")

print("\nReports Saved Successfully!")