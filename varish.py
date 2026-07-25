import pandas as pd
import numpy as np

# -----------------------------
# Create Sales Data
# -----------------------------
data = {
    "Order_ID": range(1001, 1016),
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Headphone",
        "Laptop", "Mouse", "Keyboard", "Monitor", "Headphone",
        "Laptop", "Mouse", "Keyboard", "Monitor", "Headphone"
    ],
    "Category": [
        "Electronics","Accessories","Accessories","Electronics","Accessories",
        "Electronics","Accessories","Accessories","Electronics","Accessories",
        "Electronics","Accessories","Accessories","Electronics","Accessories"
    ],
    "Month": [
        "Jan","Jan","Feb","Feb","Mar",
        "Mar","Apr","Apr","May","May",
        "Jun","Jun","Jul","Jul","Aug"
    ],
    "Quantity": [3,10,5,2,6,4,8,7,3,9,5,12,6,4,8],
    "Price": [65000,500,1500,18000,2500,66000,550,1600,18500,2600,67000,600,1700,19000,2700],
    "Cost": [58000,350,1100,15000,1800,59000,380,1200,15500,1900,60000,400,1250,16000,2000],
    "Rating": [4.8,4.2,4.5,4.6,4.1,4.9,4.3,4.4,4.7,4.0,5.0,4.2,4.5,4.8,4.3]
}

df = pd.DataFrame(data)

# -----------------------------
# Calculations
# -----------------------------
df["Revenue"] = df["Quantity"] * df["Price"]
df["Total_Cost"] = df["Quantity"] * df["Cost"]
df["Profit"] = df["Revenue"] - df["Total_Cost"]

df["Discount"] = np.where(
    df["Revenue"] > 100000,
    df["Revenue"] * 0.10,
    df["Revenue"] * 0.05
)

df["Final_Revenue"] = df["Revenue"] - df["Discount"]

# -----------------------------
# Summary
# -----------------------------
print("\n===== SALES DATA =====")
print(df)

print("\nTotal Revenue")
print(df["Final_Revenue"].sum())

print("\nTotal Profit")
print(df["Profit"].sum())

print("\nAverage Rating")
print(round(df["Rating"].mean(),2))

# -----------------------------
# Category Analysis
# -----------------------------
category = df.groupby("Category").agg({
    "Final_Revenue":"sum",
    "Profit":"sum",
    "Quantity":"sum"
})

print("\nCategory Summary")
print(category)

# -----------------------------
# Monthly Sales
# -----------------------------
monthly = df.groupby("Month")["Final_Revenue"].sum()

print("\nMonthly Revenue")
print(monthly)

# -----------------------------
# Top 5 Products
# -----------------------------
top = df.groupby("Product")["Final_Revenue"].sum().sort_values(ascending=False)

print("\nTop Products")
print(top.head())

# -----------------------------
# Pivot Table
# -----------------------------
pivot = pd.pivot_table(
    df,
    values="Profit",
    index="Month",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print("\nProfit Pivot")
print(pivot)

# -----------------------------
# Best Rated Products
# -----------------------------
best = df.sort_values("Rating", ascending=False)

print("\nBest Rated Products")
print(best[["Product","Rating"]].head())

# -----------------------------
# Export Reports
# -----------------------------
df.to_csv("sales_report.csv", index=False)
category.to_csv("category_summary.csv")
monthly.to_csv("monthly_revenue.csv")
pivot.to_csv("profit_pivot.csv")

print("\nReports Generated Successfully!")