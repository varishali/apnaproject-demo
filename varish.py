import pandas as pd

students = {
    "Roll Number" : [101,102,103,104,105],
    "Name" : ["Varish","Ali","Aman","Sohil","Sana"],
    "Python" : [90,85,89,78,75],
    "SQL" : [89,79,50,89,90],
    "Attendemce" : [95,90,85,98,92]

}

df = pd.DataFrame(students)

# totla makrs
df["Total"] = df["Python"] + df["SQL"]

# average
df["Average"] = df["Total"]/2

# grade
df["Grade"] = df["Average"].apply(
    lambda x: "A" if x>= 90 else
              "B" if x>= 80 else
              "C" if x>= 70 else
              "Fail"
)
print("\n\033[1;92m                   ------- STUDENT REPORT  --------\033[0m\n")
print(df)

print("\n\033[1;92m----- Top Student -----\033[0m\n")
print(df.loc[df["Total"].idxmax()])

print("\n\033[1;92m----- Average Python Marks -----\033[0m\n")
print(df["Python"].mean())

print("\n\033[1;92m---- Sorted by Total Marks ----\033[0m\n")
print(df.sort_values(by="Total",ascending=False))