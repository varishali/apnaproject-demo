import pandas as pd

employee = {
    "ID" : [1,2,3,4,5],
    "Name" : ["Aman","Varish","Ali","Rahul","Sara"],
    "Department" : ["IT","HR","IT","Sales","HR",],
    "Salary" : [50000,70000,65000,45000,55000],
    "Experience" : [2,5,4,1,3]
}

df = pd.DataFrame(employee)

print("\n\033[1;101m||------------ EMPLOYEE DATA -------------||\033[0m\n")
print("\033[0;92m",df,"\033[0m")

print("\n\033[1;104m|-- Highest Salary --|\033[0m\n")
top = df.loc[df["Salary"].idxmax()]
print(f"""
Name       :{top['Name']}
Department :{top['Department']}
Salary     :{top['Salary']}
""")

print("\n\033[0;104m|-- Lowest Salary --|\033[0m\n")
print(df.loc[df["Salary"].idxmin()])

print("\n\033[0;104m|-- Average Salary --|\033[0m\n")
print(df["Salary"].mean())

print("\n\033[0;104m|-- Department Wise Average Salary --|\033[0m\n")
print(df.groupby("Department")["Salary"].mean())

df["Bonus"] = df["Salary"] * 0.10
df["Final Salary"] = df["Salary"] + df["Bonus"]

print("\n\033[0;104m|-- Salary After Bonus --|\033[0m\n")
print("\033[0;92m",df,"\033[0m")

df.to_csv("employee_salary.csv",index=False)
print("\n\033[0;104m|-- File Saved --|\033[0m\n")