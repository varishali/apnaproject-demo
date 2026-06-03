students = {
    "Ali": 78,
    "Rahul": 92,
    "Sahil": 65,
    "Aman": 85
}

average = sum(students.values()) / len(students)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Average Marks:", average)
print("Topper:", highest, students[highest])
print("Lowest:", lowest, students[lowest])

print("\nGrades")

for name, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print(name, "-", grade)