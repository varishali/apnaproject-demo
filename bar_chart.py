import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Player" : ["Virat","Gill","Rohil","KL rahul"],
    "Runs" : [120,89,78,101]
}
df = pd.DataFrame(data)

# Grafh
plt.bar(df["Player"],df["Runs"])

# Grafh Title
plt.title("Player Runs")

plt.show()