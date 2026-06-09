import matplotlib.pyplot as plt
import pandas as pd
names = ["a","b","c","d","e"]
marks = [20,40,30,55,70]

df = pd.DataFrame({"names":names,"marks":marks})

plt.figure(facecolor="lightblue",figsize=(8,5))
plt.gca().set_facecolor("lightyellow")

plt.plot(df["names"],df["marks"],marker="o",color="lightcoral")

plt.grid(linestyle="--",color="gray")
plt.title(
    "Marks of students",
    color="red",
    fontweight="bold",
    fontstyle="italic",
    bbox=dict(facecolor="lightgreen",boxstyle="round")
    )
plt.xlabel("Names",
           color="red",
           fontstyle="italic",
           fontweight="bold",
           bbox=dict(facecolor="lightgreen",boxstyle="round")
           )
plt.ylabel("Marks"
           ,color="red",
           fontstyle="italic",
           fontweight="bold",
           bbox=dict(facecolor="lightgreen",boxstyle="round"))
plt.show()