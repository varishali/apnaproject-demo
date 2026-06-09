import pandas as pd
import matplotlib.pyplot as plt

data = {
    "video" : [
        "Python Tutorial",
        "Pandas basics",
        "Matplotlib Graph",
        "OOP Project",
        "Numpy Guide" 
    ],
    "views" : [1200,1800,1500,2200,1700],
    "likes" : [150,250,200,300,240]
}

df = pd.DataFrame(data)
print("\n=== Youtube Analytics ===")
print(df)

plt.title("youtube video views")
plt.xlabel("video")
plt.ylabel("views")
plt.xticks(rotation=20)
plt.show()