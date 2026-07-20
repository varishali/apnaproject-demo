import pandas as pd

# Read CSV files
emp = pd.read_csv("employee.csv")
bonus = pd.read_csv("bonus.csv")

print("\n========= EMPLOYEE DATA =========\n")
print(emp)

# Merge DataFrames
df = pd.merge(emp, bonus, on="Department")

# Total Salary
df["Total Salary"] = df["Salary"] + df["Bonus"]

# Performance Grade
df["Grade"] = df["Rating"].apply(
    lambda x: "Excellent" if x >= 4.5
    else "Good" if x >= 4
    else "Average"
)

print("\n========= MERGED DATA =========\n")
print(df)

# Average salary department wise
print("\nAverage Salary Department Wise\n")
print(df.groupby("Department")["Salary"].mean())

# Highest salary employee
print("\nHighest Salary Employee\n")
print(df.loc[df["Salary"].idxmax()])

# Top Rated Employees
print("\nTop Rated Employees\n")
print(df[df["Rating"] > 4.5])

# Pivot Table
print("\nPivot Table\n")
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Grade",
    aggfunc="mean",
    fill_value=0
)
print(pivot)

# Sort
print("\nSorted by Total Salary\n")
print(df.sort_values(by="Total Salary", ascending=False))

# Query
print("\nEmployees with Salary > 55000\n")
print(df.query("Salary > 55000"))

# Rank
df["Rank"] = df["Salary"].rank(ascending=False)

print("\nSalary Ranking\n")
print(df[["Name", "Salary", "Rank"]])

# Department Summary
summary = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Rating": "mean",
    "Experience": "sum"
})

print("\nDepartment Summary\n")
print(summary)

# Save Result
df.to_csv("employee_analysis.csv", index=False)

print("\nAnalysis Completed Successfully")