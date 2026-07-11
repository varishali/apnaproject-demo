import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month",columns="year",values="passengers")
sns.heatmap(
    flights_pivot,
    cmap="coolwarm",
    annot=True,
    fmt="d"
)

plt.title("Passengers Heatmap")
plt.tight_layout()
plt.show()

