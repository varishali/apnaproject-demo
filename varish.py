import pandas as pd

# CSV file read
df = pd.read_csv("data.csv")

print("\n========== STUDENT RESULT ANALYZER ==========\n")

# Complete data
print("Student Data:\n")
print(df)

# Total Marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

# Percentage
df["Percentage"] = (df["Total"] / 300) * 100

# Result
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Grade
def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(grade)

print("\n========== UPDATED RESULT ==========\n")
print(df)

# Topper
topper = df.loc[df["Percentage"].idxmax()]

print("\n========== TOPPER ==========")
print(topper)

# Average Marks
print("\nAverage Marks")
print(df[["Math", "Science", "English"]].mean())

# Highest Marks
print("\nHighest Marks")
print(df[["Math", "Science", "English"]].max())

# Lowest Marks
print("\nLowest Marks")
print(df[["Math", "Science", "English"]].min())

# Course Wise Average
print("\n========== COURSE WISE AVERAGE ==========")
print(df.groupby("Course")[["Math","Science","English","Percentage"]].mean())

# Attendance > 90
print("\n========== ATTENDANCE ABOVE 90 ==========")
print(df[df["Attendance"] > 90][["Name","Attendance"]])

# Students Scoring Above 80%
print("\n========== STUDENTS ABOVE 80% ==========")
print(df[df["Percentage"] >= 80][["Name","Course","Percentage","Grade"]])

# Sort by Percentage
print("\n========== RANK LIST ==========")
print(df.sort_values(by="Percentage", ascending=False)[["Name","Percentage","Grade"]])

# Save Result
df.to_csv("student_result.csv", index=False)

print("\nResult saved successfully as student_result.csv")

df = pd.read_csv("student_result.csv")
print(df)