import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Marks" : [23,5,67,78,55,77,88]
}
df = pd.DataFrame(data)

plt.hist(df["Marks"])

plt.title("Marks Distribution")

plt.show()