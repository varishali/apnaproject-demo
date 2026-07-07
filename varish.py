import matplotlib.pyplot as plt

# Months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Department Profit
departments = {
    "IT": [45, 50, 55, 60, 58, 65],
    "HR": [15, 18, 20, 22, 21, 23],
    "Sales": [35, 40, 38, 45, 50, 55]
}

# Total Profit Calculate
total_profit = []

for i in range(len(months)):

    total = 0

    for dept in departments:

        total += departments[dept][i]

    total_profit.append(total)

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# ---------------- IT ----------------
axes[0][0].plot(months, departments["IT"], marker="o")
axes[0][0].set_title("IT Department")
axes[0][0].grid(True)

# ---------------- HR ----------------
axes[0][1].bar(months, departments["HR"])
axes[0][1].set_title("HR Department")
axes[0][1].grid(True)

# -------------- Sales ---------------
axes[1][0].plot(months, departments["Sales"], marker="s")
axes[1][0].set_title("Sales Department")
axes[1][0].grid(True)

# -------- Total Profit --------------
axes[1][1].pie(
    total_profit,
    labels=months,
    autopct="%1.1f%%"
)
axes[1][1].set_title("Monthly Profit Share")

fig.suptitle("Company Profit Dashboard")

plt.tight_layout()

plt.show()