def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter Student Name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter Marks of Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5
grade = calculate_grade(percentage)

print("\n------ RESULT ------")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)