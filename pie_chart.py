import pandas as pd 
import matplotlib.pyplot as plt
data = {
    "Runs" : [120,56,89],
    "Player" : ["virat","rohit","gill"]
}
df = pd.DataFrame(data)

# percentage
plt.pie(df["Runs"],labels=df["Player"])

# title
plt.title("Runs Share")

plt.show()