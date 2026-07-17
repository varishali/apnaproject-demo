import pandas as pd

# read csv
df = pd.read_csv("file.csv")

print("\n----------------- Employee Salary Analyzer ------------------\n")

# show data
print("---------------------- Employee Data ------------------------")
print(df)


# highest salary
print("\nHighest Salary Employee : ")
print(df.loc[df["Salary"].idxmax()])

# lowest salary
print("\nLowest Salary Employee : ")
print(df.loc[df["Salary"].idxmin()])

# avarage salary
print("\nAverage Salary : ",round(df["Salary"].mean(),2))

