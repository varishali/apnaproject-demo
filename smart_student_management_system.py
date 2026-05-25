import pandas as pd
import matplotlib.pyplot as plt

# student data
data = {
    "Name" : ["Varish","Sohil","Ali","Zainul","Aman","Faizan"],
    "City" : ["Dehli","Noida","Dehli","Lucknow","Noida","Dehli"],
    "Marks" : [95,45,72,88,60,30],
    "Attendence" : [90,65,80,95,70,50]
}
# data frame
df = pd.DataFrame(data)

# pass fail list
result = []
# grade list
grades = []

# loop + if alse
for marks in df["Marks"]:

    # fail pass
    if marks >= 50:
        result.append("Pass")
    else:
        result.append("Fail")

    # grades
    if marks >= 90:
        grades.append("A")

    elif marks >= 75:
        grades.append("B") 

    elif marks >= 50:
        grades.append("C")

    else:
        grades.append("F")

# new column
df["Result"] = result
df["Grades"] = grades

# bonus marks using apply lambda
df["Bonus_marks"] = df["Marks"].apply(lambda x: x+5)

# heading
print("\033[1;92m")
print("=" *55)
print("           SMART STUDENT MANAGEMENT SYSTEM")
print("=" *55)
print("\033[0m")

# full data
print("\n\033[1;93mFull Student Data\033[0m\n")
print(df)

# basic statistics
print("\nAverage Marks : ")
print(df["Marks"].mean())

print("\nHighest Marks : ")
print(df["Marks"].max())

print("\nLowest Marks : ")
print(df["Marks"].min())

print("\nTotal Marks : ")
print(df["Marks"].sum())

print("\nTotal Student : ")
print(df["Name"].count())

# describe
print("\nFull Statistics : ")
print(df.describe())

# filtering
print("\nStudent Scoring Above 70 : \n")
print(df[df["Marks"] > 70])

# multiple condition filter
print("\nDehli student above 50 marks : \n")
print(df[(df["City"] == "Dehli") & (df["Marks"] > 50)])

# sorting
print("\nSort by marks : \n")
print(df.sort_values("Marks",ascending=False))

# groupby
print("\nCity wise average mrks : \n")
print(df.groupby("City")["Marks"].mean())

# bar grafh
plt.bar(df["Name"],df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()

print("\n" +"=" *55)
print("                 Analysis Completed")
print("=" *55)