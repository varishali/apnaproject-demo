import seaborn as sns
import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sales = [20,30,40,10,35]

sns.lineplot(
    x=days,
    y=sales,
    marker="o",
    color="blue"
)
plt.title("Daily Sales")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid()
plt.show()