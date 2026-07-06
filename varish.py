import matplotlib.pyplot as plt


# Students
students = [

    "Ali",

    "Varish",

    "Aman",

    "Rohan",

    "Zaid"
]


# Subject marks
python_marks = [80, 92, 75, 88, 95]

sql_marks = [70, 85, 78, 82, 90]

ml_marks = [90, 89, 80, 91, 93]


# Create figure
fig, axes = plt.subplots(1, 3)


# ==================================
# PYTHON GRAPH
# ==================================
axes[0].plot(

    students,

    python_marks,

    marker="o"
)

axes[0].set_title("Python")

axes[0].grid(True)


# ==================================
# SQL GRAPH
# ==================================
axes[1].bar(

    students,

    sql_marks
)

axes[1].set_title("SQL")

axes[1].grid(True)


# ==================================
# MACHINE LEARNING GRAPH
# ==================================
axes[2].scatter(

    students,

    ml_marks
)

axes[2].set_title("Machine Learning")

axes[2].grid(True)


# Main title
fig.suptitle("Student Performance Analytics")


# Auto spacing
fig.tight_layout()


# Show graphs
plt.show()