import matplotlib.pyplot as plt

# Departments
departments = ["ICU", "Emergency", "General", "Pediatrics", "Surgery"]

# Data
patients = [35, 60, 45, 30, 40]
doctors = [10, 15, 12, 8, 11]
beds = [40, 70, 50, 35, 45]

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Patients

axes[0][0].bar(departments, patients)
axes[0][0].set_title("Patients")
axes[0][0].grid(True)

# Doctors

axes[0][1].plot(departments, doctors, marker="o")
axes[0][1].set_title("Doctors")
axes[0][1].grid(True)

# Beds

axes[1][0].scatter(departments, beds)
axes[1][0].set_title("Available Beds")
axes[1][0].grid(True)

# Occupancy Percentage

occupancy = []

for i in range(len(departments)):
    percentage = (patients[i] / beds[i]) * 100
    occupancy.append(percentage)

axes[1][1].plot(departments, occupancy, marker="*", linewidth=2)
axes[1][1].set_title("Bed Occupancy %")
axes[1][1].grid(True)

# Main Title
fig.suptitle("Hospital Management Dashboard")

plt.tight_layout()

plt.show()