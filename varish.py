import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(type(tips))


print(tips.head())

sns.barplot(
    data=tips,
    x="day",
    y="tip",
    hue="sex"
)
plt.show()