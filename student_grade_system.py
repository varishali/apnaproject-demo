import pandas as pd
data = {
    "Name" : ["variah","ali","sohil","zainul","aman"],
    "Marks" : [98,90,67,86,45]
}
# data frame 
df = pd.DataFrame(data)

# empty list ufor grade
grades = []

# loop 
for marks in df["Marks"]:

    if marks >= 90:
        grades.append("A")

    elif marks >= 75:
        grades.append("B")
    
    elif marks >= 50:
        grades.append("C")

    else:
        grades.append("Fail")    

# add new collumn
df["Grade"] = grades

# heading
print("=" *40)
print("         STUDENT GRADE SYSTEM")
print("=" *40)

# FULL DATA
print("\nStudent Data :\n")
print(df)