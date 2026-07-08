import matplotlib.pyplot as plt

# Days
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Room Names
rooms = ["Hall", "Kitchen", "Bedroom", "Bathroom"]

# Electricity Units (kWh)
units = [
    [12, 14, 13, 15, 16],   # Hall
    [8, 9, 10, 9, 11],       # Kitchen
    [6, 7, 8, 7, 9],         # Bedroom
    [3, 4, 3, 5, 4]          # Bathroom
]

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

room = 0

for i in range(2):

    for j in range(2):

        axes[i][j].bar(
            days,
            units[room]
        )

        axes[i][j].set_title(rooms[room])

        axes[i][j].set_xlabel("Days")

        axes[i][j].set_ylabel("Electricity (kWh)")

        axes[i][j].grid(True)

        room += 1

# Main Title
fig.suptitle("Electricity Consumption Dashboard")

# Auto Spacing
plt.tight_layout()

# Show Graph
plt.show()