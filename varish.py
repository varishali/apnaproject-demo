import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Marks" : [78,90,67,88],
    "Attendance" : [90,95,70,85],
    "Study" : [2,5,1,4]
}
df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()