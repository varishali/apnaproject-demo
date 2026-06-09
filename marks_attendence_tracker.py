import matplotlib.pyplot as plt
import pandas as pd
names = ["a","b","c","d","e"]
marks = [79,40,30,55,70]
attendence = [60,70,85,60,75,]

df = pd.DataFrame({"names":names,"marks":marks,"attendence":attendence})

plt.figure(facecolor="lightblue",figsize=(8,5))
plt.gca().set_facecolor("lightyellow")

plt.plot(df["names"],df["marks"],marker="o",color="lightcoral",label="Marks")
plt.plot(df["names"],df["attendence"],marker="s",color="lightgreen",label="Attendence")

plt.legend(loc="upper left",
           title="Student Data")

plt.grid(linestyle="--",color="gray")
plt.title(
    "Marks of students",
    color="red",
    fontweight="bold",
    fontstyle="italic",
    bbox=dict(facecolor="lightgreen",boxstyle="round4")
    )
plt.xlabel("Students",
           color="red",
           fontstyle="italic",
           fontweight="bold",
           bbox=dict(facecolor="lightgreen",boxstyle="round4")
           )
plt.ylabel("Values"
           ,color="red",
           fontstyle="italic",
           fontweight="bold",
           bbox=dict(facecolor="lightgreen",boxstyle="round4"))

plt.show()