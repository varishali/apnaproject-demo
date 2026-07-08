import matplotlib.pyplot as plt

# Weeks
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]

# Plant Names
plants = ["Rose", "Sunflower", "Tulip", "Lily"]

# Growth Data (cm)
growth = [
    [5, 8, 11, 15, 19],      # Rose
    [6, 10, 15, 21, 27],     # Sunflower
    [4, 6, 9, 12, 16],       # Tulip
    [5, 7, 10, 13, 17]       # Lily
]

# Create 2x2 Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

plant = 0

for i in range(2):
    for j in range(2):

        axes[i][j].plot(
            weeks,
            growth[plant],
            marker="o",
            linewidth=2
        )

        axes[i][j].set_title(plants[plant])
        axes[i][j].set_xlabel("Weeks")
        axes[i][j].set_ylabel("Height (cm)")
        axes[i][j].grid(True)

        plant += 1

fig.suptitle("Plant Growth Analysis")

plt.tight_layout()

plt.show()