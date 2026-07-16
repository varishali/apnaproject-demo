import pandas as pd

# -----------------------------
# Employee Data
# -----------------------------
employees = pd.DataFrame({
    "EmpID": [101,102,103,104,105],
    "Name": ["Aman","Riya","Karan","Neha","Vikas"],
    "Dept": ["IT","HR","IT","Finance","HR"],
    "Salary": [50000,45000,60000,70000,48000],
    "Age": [25,30,28,35,27]
})

# Department Data
departments = pd.DataFrame({
    "Dept": ["IT","HR","Finance"],
    "Manager": ["Raj","Priya","Ankit"]
})

# -----------------------------
# Merge
# -----------------------------
df = pd.merge(employees, departments, on="Dept")

# -----------------------------
# New Column
# -----------------------------
df["Bonus"] = df["Salary"] * 0.10
df["TotalSalary"] = df["Salary"] + df["Bonus"]

# -----------------------------
# Filter
# -----------------------------
high_salary = df[df["Salary"] > 50000]

# -----------------------------
# Sort
# -----------------------------
sorted_df = df.sort_values("Salary", ascending=False)

# -----------------------------
# GroupBy
# -----------------------------
group = df.groupby("Dept").agg({
    "Salary": ["mean","max","min","sum"],
    "Age": "mean"
})

# -----------------------------
# Pivot Table
# -----------------------------
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Dept",
    columns="Manager",
    aggfunc="mean"
)

# -----------------------------
# Ranking
# -----------------------------
df["Rank"] = df["Salary"].rank(ascending=False)

# -----------------------------
# Apply + Lambda
# -----------------------------
df["Tax"] = df["Salary"].apply(lambda x: x*0.05)

# -----------------------------
# Query
# -----------------------------
query_result = df.query("Age > 27")

# -----------------------------
# MultiIndex
# -----------------------------
multi = df.set_index(["Dept","Name"])

# -----------------------------
# Missing Values
# -----------------------------
df.fillna(0, inplace=True)

# -----------------------------
# Output
# -----------------------------
print("Original Data")
print(df)

print("\nHigh Salary")
print(high_salary)

print("\nSorted")
print(sorted_df)

print("\nGroupBy")
print(group)

print("\nPivot Table")
print(pivot)

print("\nQuery Result")
print(query_result)

print("\nMultiIndex")
print(multi)

