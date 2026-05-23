import pandas as pd

# Employee Data
data = {
    "EMPLOYEE": ["Aman", "Varish", "Sohil", "Zainul", "Ali"],
    "SALARY": [45000, 60000, 38000, 72000, 50000],
    "DEPARTMENT": ["IT", "HR", "IT", "Manager", "Sales"]
}

# DataFrame
df = pd.DataFrame(data)

# Stylish Heading
print("\033[1;96m")
print("=" * 45)
print("         EMPLOYEE SALARY ANALYZER")
print("=" * 45)
print("\033[0m")

# Full Data
print("\n\033[1;93m[EMPLOYEE DATA]\033[0m\n")
print(df)

# Average Salary
print("\nAverage Salary:")
print(df["SALARY"].mean())

# Highest Salary
print("\nHighest Salary:")
print(df["SALARY"].max())

# Lowest Salary
print("\nLowest Salary:")
print(df["SALARY"].min())

# Total Salary
print("\nTotal Salary:")
print(df["SALARY"].sum())

# High Salary Employees
print("\n\033[1;92mEmployees Salary Greater Than 50000:\033[0m\n")
print(df[df["SALARY"] > 50000])

# Sorting
print("\n\033[1;95mEmployees Sorted By Salary:\033[0m\n")
print(df.sort_values("SALARY", ascending=False))

# iloc Example
print("\n\033[1;94mFirst Employee Details:\033[0m\n")
print(df.iloc[0])

print("\n" + "=" * 45)
print("            ANALYSIS COMPLETED")
print("=" * 45)