import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Product" : ["Laptop","Keyboard","Phone","Mouse","Tablet","Watch"],
    "Price" : [50000,500,25000,250,20000,700],
    "Sales" : [5,7,10,6,20,25]
}
df = pd.DataFrame(data)

# random discount
df["Discount"] = np.random.randint(5,26,size=len(df))

# final price
df["Final_Price"] = df["Price"] - (df["Sales"]*df["Discount"]/100)

# total revanue
df["Revanue"] = df["Final_Price"] * df["Sales"]

# catagory list
category = []
for revanue in df["Revanue"]:
    if revanue >= 200000:
        category.append("High")

    elif revanue >= 50000:
        category.append("Medium")

    else:
        category.append("Low")

# new_column
df["Category"] = category

# heading
print("\n" + "=" * 55)
print("              SMART SALES ANALYZSIS SYSTEM")
print("=" * 55)

#full data
print("\nFULL PRODUCT DATA : \n")
print(df)

# statistics
print("\nAvarage Revanue : ")
print(np.mean(df["Revanue"]))

print("\nHighest Revanue : ")
print(np.max(df["Revanue"]))

print("\nLowest Reavanue : ")
print(np.min(df["Revanue"]))

# high revanue product
print("\nHigh Reavanue Product : ")
print(df[df["Category"] == "High"])

# graph size 
plt.figure(figsize=(7,5),facecolor="gray")

# bar graph
plt.bar(
    df["Product"],
    df["Revanue"],
    color="cyan"
)

# graph background
plt.axes().set_facecolor("pink")

# title
plt.title(
    "Product Revanue Analysis",
    fontsize=18,
    color="white",
    fontweight="bold",
    bbox={
        "facecolor" : "red",
        "edgecolor" : "white",
        "boxstyle" : "round"
    }
)

plt.plot(df["Price"],df["Sales"])
# label
plt.xlabel("Product",color="white")
plt.ylabel("Revanue",color="white")

#grid
plt.grid(color="white",linestyle=":")

# author name
plt.text(
    0,
    max(df["Revanue"]),
    "By VARISH",
    color="yellow",
    fontsize=12,
    fontstyle="italic"

)

plt.show()

print("\nANALYSIS COMPLETED....")