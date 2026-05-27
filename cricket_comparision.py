import matplotlib.pyplot as plt

matches = [1,2,3,4,5,6]
virat = [45,67,90,35,50,100]
rohit = [30,50,40,78,95,85]

plt.figure(figsize=(8,5))
plt.axes().set_facecolor("pink")
plt.plot(matches,virat,label="virat",marker="o",color="red",markerfacecolor="green",
         markeredgecolor="black",alpha=0.5)
plt.plot(matches,rohit,label="rohit",marker="*",color="green",markerfacecolor="red",
         markeredgecolor="black",alpha=0.5)

plt.title("Player Comparision",color="blue",fontstyle="italic",fontweight="bold",
          bbox={
              "facecolor":"yellow",
              "edgecolor":"black",
              "boxstyle":"round"
          })

plt.xlabel("Matches",color="blue",fontstyle="italic",fontweight="bold",
           bbox={
               "facecolor":"yellow",
               "edgecolor":"black",
               "boxstyle":"round"
           })

plt.ylabel("Runs",color="blue",fontstyle="italic",fontweight="bold",
           bbox={
               "facecolor":"yellow",
               "edgecolor":"black",
               "boxstyle":"round"
           })

plt.legend()

plt.grid(linestyle="--",color="white")

plt.text(3.2,65,"By Varish",fontweight="bold",alpha=0.2)

plt.show()