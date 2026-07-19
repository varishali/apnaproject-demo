import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [50000, 65000, 70000, 85000, 90000, 100000]
expenses = [30000, 35000, 40000, 45000, 50000, 55000]

# Profit
profit = []
for s, e in zip(sales, expenses):
    profit.append(s - e)

# -------- Line Chart --------
plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', linewidth=2, label="Sales")
plt.plot(months, expenses, marker='s', linewidth=2, label="Expenses")
plt.title("Monthly Sales vs Expenses")
plt.xlabel("Months")
plt.ylabel("Amount (₹)")
plt.legend()
plt.grid(True)
plt.show()

# -------- Bar Chart --------
plt.figure(figsize=(8,5))
plt.bar(months, profit)
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit (₹)")
plt.grid(axis="y")
plt.show()

# -------- Pie Chart --------
labels = ["Sales", "Expenses"]
values = [sum(sales), sum(expenses)]

plt.figure(figsize=(6,6))
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Sales vs Expenses Distribution")
plt.show()