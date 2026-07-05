import matplotlib.pyplot as plt

expenses = ["er","wt","as","ui","op"]
amounts = [500,150,120,100,50]

plt.style.use("default")
explode = [0,0,0,0.2,0]
plt.pie(amounts,
        labels=expenses,
        autopct="%1.1f%%",
        explode=explode,
        shadow=True)
plt.show()