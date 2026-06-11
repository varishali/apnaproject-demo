import matplotlib.pyplot as plt

match = [1,2,3,4,5,6]
virat = [45,67,89,64,100,20]
rohit = [60,30,78,59,80,90]

plt.figure(figsize=(10,5))
plt.plot(match,virat,
         label="virat",color="red",linestyle="--",
         marker="o",linewidth="3",markersize=15,markerfacecolor="green",
         markeredgecolor="black")
plt.plot(match,rohit,
         label="rohit",color="blue",linestyle=":",
         marker="*",linewidth="2",markersize=15,markerfacecolor="green",
         markeredgecolor="yellow")

plt.title("Player performance")
plt.xlabel("Mathes")
plt.ylabel("Runs")
plt.legend()
plt.grid(linestyle=":")

plt.show()