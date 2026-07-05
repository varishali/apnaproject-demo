import matplotlib.pyplot as plt

people = ["P A","P B","P C","P D","P E",
          "P F","P G","P H","P I","P J"]

age = [22,25,30,35,40,45,50,55,60,65]
bp = [110,115,120,122,125,130,135,123,145,150]

colors = ["green" if x < 135 else "red" for x in bp]

plt.scatter(age,bp, s=bp, cmap="plasma",c=bp)
plt.title("Age vs BP")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")

plt.grid()
plt.colorbar(label="BP")
for i in range(len(people)):
    plt.annotate(people[i], xy=(age[i], bp[i]), xytext=(age[i]+1,bp[i]+1))

plt.xlim(min(age),max(age)+10)
plt.ylim(min(bp),max(bp)+5)

plt.show()