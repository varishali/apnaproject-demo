import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,5))

fig.patch.set_facecolor("black")

ax.set_facecolor("black")

# moon
moon = plt.Circle(
    (0.5,0.5),
    (0.2),
    color="yellow"
)

# cut part
cut = plt.Circle(
    (0.58,0.55),
    0.2,
    color="black"
)
ax.add_patch(moon)
ax.add_patch(cut)

# text
plt.text(
    0.2,
    0.2,
    "EID MUBARAK",
    fontsize=28,
    color="cyan",
    fontweight="bold" 
)

plt.axis("off")

plt.show()