import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri"]

cities = ["New York","London","Dehli","Tokyo"]

tempratures = [
    [22,23,21,24,25],  # New York
    [18,19,17,20,21],  # london
    [30,32,31,33,34],  # Dehli
    [25,26,24,27,28]   # Tokyo
]
fig, axes = plt.subplots(2, 2)

city_no = 0
for i in range(2):
    for j in range(2):
        axes[i][j].plot(days, tempratures[city_no],marker='o')
        axes[i][j].set_title(cities[city_no])
        axes[i][j].grid(True)
        city_no = city_no + 1
fig.suptitle("Tempratures in cities over the week")   
fig.supylabel("Tempretures")
fig.supxlabel("Days")
fig.tight_layout()
plt.show()
