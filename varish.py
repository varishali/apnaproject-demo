import pandas as pd
import os

FILE = "students.csv"

# Create CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame({
        "ID": [1, 2, 3, 4, 5],
        "Name": ["Aman", "Rahul", "Priya", "Neha", "Rohan"],
        "Math": [85, 72, 91, 68, 77],
        "Science": [80, 75, 95, 70, 82],
        "English": [78, 88, 90, 72, 79]
    })
    df.to_csv(FILE, index=False)

# Read CSV
df = pd.read_csv(FILE)

# Total & Average
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = (df["Total"] / 3).round(2)

# Grade
def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(grade)

print("\n===== STUDENT REPORT =====")
print(df)

print("\nTop Student:")
print(df.loc[df["Total"].idxmax()])

print("\nClass Statistics")
print("Highest Total :", df["Total"].max())
print("Lowest Total  :", df["Total"].min())
print("Average Marks :", round(df["Average"].mean(), 2))

# Save result
df.to_csv("student_result.csv", index=False)

print("\nResult saved as 'student_result.csv'")