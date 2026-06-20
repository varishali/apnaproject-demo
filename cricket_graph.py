# matplotlib library import
import matplotlib.pyplot as plt

# path effect/shadow effects ke liye module import
import matplotlib.patheffects as pe

# X-axis (match number)
match = [1,2,3,4,5,6]

# virat ke runs
virat = [90,67,36,78,45,10]
# rohit ke runs
rohit = [50,45,100,12,79,25]
# rahul ke runs
klrahul = [10,34,56,95,12,89]

# figure
plt.figure(figsize=(8,5),facecolor="lightcyan")

# virat ka line graph
plt.plot(
    match,virat,label="virat",
    color="red",linestyle="--",marker="o",markerfacecolor="white",
    markeredgecolor="black"
    )

# rohit ka line graph
plt.plot(
    match,rohit,label="rohit",
    color="blue",linestyle=":",marker="*",markerfacecolor="white",
    markeredgecolor="black"
    )

# rahul ka line graph
plt.plot(
    match,klrahul,label="klrahul",
    color="green",linestyle="--",marker="s",markerfacecolor="white",
    markeredgecolor="black",    
    )

# current graph erea ko exis karna
ax = plt.gca()
# graph ke andar ka background color
ax.set_facecolor("lavender")

# graph title
plt.title("== RUNS PER MATCH ==",fontstyle="italic",pad=15,
          path_effects=[pe.withStroke(linewidth=4,foreground="gray")
          ],
          bbox={
              "facecolor":"lightblue",
              "edgecolor":"aliceblue",
              "boxstyle":"round"
          })

# X-exis label
plt.xlabel("MATCH",fontstyle="italic",
            path_effects=[pe.withStroke(linewidth=4,foreground="gray")
                     ],
           bbox={
               "facecolor":"lightblue",
               "edgecolor":"aliceblue",
               "boxstyle":"round"
           })

# Y-axis label
plt.ylabel("RUNS",fontstyle="italic",
            path_effects=[pe.withStroke(linewidth=4,foreground="gray")
                     ],
           bbox={
               "facecolor":"lightblue",
               "edgecolor":"aliceblue",
               "boxstyle":"round"
           })

# legend/info box
plt.legend(facecolor="lightblue",
    shadow=True,loc="upper right",frameon=True,edgecolor="black")

# grid line show karna
plt.grid(linestyle="--",alpha=0.5)

# final graph screen par dikhana
plt.show()