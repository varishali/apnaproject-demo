import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Match" : [1,2,3,4,5,6],
    "Runs" :[34,56,101,90,76,110]
}
df = pd.DataFrame(data)

# LINE GRAFH 
plt.plot(df["Match"],df["Runs"])

# TITLE
plt.title("Runs Per Match")

# X- AXIS
plt.xlabel("Match")

# Y-AXIS
plt.ylabel("Runs")

# GRAFH DISPLAY
plt.show()