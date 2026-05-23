import pandas as pd

# Mobile Store Data
data = {
    "MOBILE": ["iPhone 15", "Samsung S24", "OnePlus 12", "Realme GT", "Redmi Note"],
    "PRICE": [80000, 75000, 65000, 35000, 20000],
    "RATING": [4.8, 4.6, 4.5, 4.2, 4.1]
}

# DataFrame
df = pd.DataFrame(data)

# Stylish Heading
print("\033[1;96m")
print("=" * 45)
print("           MOBILE STORE ANALYZER")
print("=" * 45)
print("\033[0m")

# Full Data
print("\n\033[1;93m[MOBILE DATA]\033[0m\n")
print(df)

# Average Price
print("\nAverage Price:")
print(df["PRICE"].mean())

# Highest Price
print("\nHighest Price:")
print(df["PRICE"].max())

# Lowest Price
print("\nLowest Price:")
print(df["PRICE"].min())

# Average Rating
print("\nAverage Rating:")
print(df["RATING"].mean())

# Expensive Mobiles
print("\n\033[1;92mMobiles Price Greater Than 50000:\033[0m\n")
print(df[df["PRICE"] > 50000])

# Sorting
print("\n\033[1;95mMobiles Sorted By Price:\033[0m\n")
print(df.sort_values("PRICE", ascending=False))

# iloc Example
print("\n\033[1;94mFirst Mobile Details:\033[0m\n")
print(df.iloc[0])

print("\n" + "=" * 45)
print("            ANALYSIS COMPLETED")
print("=" * 45)