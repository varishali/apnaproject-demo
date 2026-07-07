import matplotlib.pyplot as plt

# Employee Names
employees = ["Ali", "Varish", "Aman", "Rohan", "Zaid"]

# Data
salary = [30000, 45000, 50000, 42000, 55000]
experience = [1, 3, 5, 2, 6]
age = [22, 25, 28, 24, 30]
projects = [2, 5, 6, 3, 7]
rating = [3.5, 4.8, 4.2, 4.0, 4.9]

# Create Dashboard
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# Salary

axes[0][0].bar(employees, salary)
axes[0][0].set_title("Employee Salary")
axes[0][0].set_ylabel("Salary")
axes[0][0].grid(True)


# Experience

axes[0][1].plot(employees, experience, marker="o")
axes[0][1].set_title("Experience")
axes[0][1].grid(True)

# Age

axes[0][2].scatter(employees, age)
axes[0][2].set_title("Age")
axes[0][2].grid(True)


# Projects

axes[1][0].bar(employees, projects)
axes[1][0].set_title("Completed Projects")
axes[1][0].grid(True)

# Rating

axes[1][1].plot(employees, rating, marker="*", linewidth=2)
axes[1][1].set_title("Performance Rating")
axes[1][1].grid(True)


# Salary vs Experience

axes[1][2].scatter(experience, salary)
axes[1][2].set_title("Salary vs Experience")
axes[1][2].set_xlabel("Experience")
axes[1][2].set_ylabel("Salary")
axes[1][2].grid(True)

# Dashboard Title
fig.suptitle("Employee Analytics Dashboard", fontsize=16)

# Adjust Layout
plt.tight_layout()

# Show Dashboard
plt.show()