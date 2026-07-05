import matplotlib.pyplot as plt

# multiple plots
cities = ["City A","City B","City C","City D","City E"]

# winter : temprature
winter_temp = [5,2,10,0,7]
winter_humidity = [80,75,65,85,70]

# summer : temprature
summer_temp = [25,30,28,35,27]
summer_humidity = [60,50,55,45,65]

plt.scatter(winter_temp,winter_humidity, label="Winter")
plt.scatter(summer_temp,summer_humidity, label="Summer")

plt.title("Summer VS Winter Data")
plt.xlabel("Temprature")
plt.ylabel("Humidity")
plt.legend()
plt.show()