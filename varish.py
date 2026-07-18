import pandas as pd

# CSV file read
df = pd.read_csv("employee.csv")

print("========== EMPLOYEE DATA ==========\n")
print(df)

# Bonus (10%)
df["Bonus"] = df["Salary"] * 0.10

# Total Salary
df["Total Salary"] = df["Salary"] + df["Bonus"]

print("\n========== UPDATED DATA ==========\n")
print(df)

# Highest Salary
print("\nHighest Salary Employee:")
print(df.loc[df["Salary"].idxmax()])

# Lowest Salary
print("\nLowest Salary Employee:")
print(df.loc[df["Salary"].idxmin()])

# Average Salary
print("\nAverage Salary:", df["Salary"].mean())

# Department Wise Average Salary
print("\nDepartment Wise Average Salary")
print(df.groupby("Department")["Salary"].mean())

# Employees with Salary Above 50000
print("\nEmployees earning above 50000")
print(df[df["Salary"] > 50000])

# Sort by Salary
print("\nSalary Ranking")
print(df.sort_values(by="Salary", ascending=False))

# Save new file
df.to_csv("employee_report.csv", index=False)

print("\nReport saved as employee_report.csv")