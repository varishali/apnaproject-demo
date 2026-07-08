import matplotlib.pyplot as plt

# Time Slots
time = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Vehicle Types
vehicles = ["Cars", "Bikes", "Buses", "Trucks"]

# Traffic Data
traffic = [
    [250, 270, 300, 280, 310],   # Cars
    [400, 420, 390, 450, 470],   # Bikes
    [80, 85, 82, 90, 95],        # Buses
    [60, 70, 65, 75, 80]         # Trucks
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

vehicle = 0

for i in range(2):
    for j in range(2):

        axes[i][j].plot(
            time,
            traffic[vehicle],
            marker="o",
            linewidth=2
        )

        axes[i][j].set_title(vehicles[vehicle])
        axes[i][j].set_xlabel("Days")
        axes[i][j].set_ylabel("Vehicle Count")
        axes[i][j].grid(True)

        vehicle += 1

fig.suptitle("Traffic Analysis Dashboard")

plt.tight_layout()

plt.show()