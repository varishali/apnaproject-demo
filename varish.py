import matplotlib.pyplot as plt

# Products
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# Stock Data
current_stock = [120, 250, 180, 90]
sold = [80, 170, 120, 60]
remaining = [40, 80, 60, 30]
returned = [5, 8, 4, 2]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Current Stock
axes[0][0].bar(products, current_stock)
axes[0][0].set_title("Current Stock")
axes[0][0].grid(True)

# Sold Products
axes[0][1].bar(products, sold)
axes[0][1].set_title("Sold Products")
axes[0][1].grid(True)

# Remaining Stock
axes[1][0].bar(products, remaining)
axes[1][0].set_title("Remaining Stock")
axes[1][0].grid(True)

# Returned Products
axes[1][1].bar(products, returned)
axes[1][1].set_title("Returned Products")
axes[1][1].grid(True)

fig.suptitle("Warehouse Stock Dashboard")

plt.tight_layout()

plt.show()