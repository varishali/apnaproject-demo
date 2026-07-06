import matplotlib.pyplot as plt


# Months
months = [

    "Jan",

    "Feb",

    "Mar",

    "Apr",

    "May"
]


# Product sales
products = [

    "Laptop",

    "Mobile",

    "Tablet",

    "Camera"
]


sales = [

    [50, 60, 55, 70, 80],   # Laptop

    [40, 45, 50, 55, 60],   # Mobile

    [20, 25, 22, 30, 35],   # Tablet

    [15, 18, 20, 25, 28]    # Camera
]


# Create 2x2 graphs
fig, axes = plt.subplots(2, 2)


product_no = 0


# Nested loop
for i in range(2):


    for j in range(2):


        # Plot graph
        axes[i][j].bar(

            months,

            sales[product_no]
        )


        # Graph title
        axes[i][j].set_title(

            products[product_no]
        )


        # X label
        axes[i][j].set_xlabel("Months")


        # Y label
        axes[i][j].set_ylabel("Sales")


        # Grid
        axes[i][j].grid(True)


        # Next product
        product_no += 1


# Main title
fig.suptitle("Product Sales Dashboard")


# Auto spacing
fig.tight_layout()


# Show graph
plt.show()
