import pandas as pd
import numpy as np

# -------------------------------
# Sample Patient Data
# -------------------------------
data = {
    "Patient_ID":[101,102,103,104,105,106,107,108,109,110],
    "Name":["Aman","Riya","Ali","Sneha","Rohit",
            "Priya","Karan","Neha","Arjun","Sara"],
    "Age":[25,42,35,60,55,30,70,48,52,66],
    "Gender":["Male","Female","Male","Female","Male",
              "Female","Male","Female","Male","Female"],
    "Disease":["Diabetes","BP","Diabetes","Heart","BP",
               "Asthma","Heart","Diabetes","BP","Heart"],
    "Weight":[70,62,82,68,90,55,78,64,85,72],
    "Height":[1.72,1.60,1.78,1.58,1.80,1.55,1.70,1.62,1.75,1.60],
    "Bill":[12000,8500,15000,25000,9000,
            6000,28000,13000,9500,30000]
}

df = pd.DataFrame(data)

# -------------------------------
# Basic Information
# -------------------------------
print("\nPATIENT DATA\n")
print(df)

print("\nShape :", df.shape)
print("\nColumns :", list(df.columns))

# -------------------------------
# Missing Values
# -------------------------------
print("\nMissing Values\n")
print(df.isnull().sum())

# -------------------------------
# BMI Calculation
# -------------------------------
df["BMI"] = round(df["Weight"] / (df["Height"] ** 2),2)

# -------------------------------
# Risk Category
# -------------------------------
conditions = [
    df["Age"] >= 60,
    df["Age"] >= 45,
    df["Age"] >= 30
]

choices = ["High","Medium","Low"]

df["Risk"] = np.select(conditions, choices, default="Very Low")

# -------------------------------
# Age Group
# -------------------------------
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0,18,35,50,100],
    labels=["Child","Young","Adult","Senior"]
)

# -------------------------------
# Disease Wise Count
# -------------------------------
print("\nDisease Count\n")
print(df["Disease"].value_counts())

# -------------------------------
# Gender Wise Average Bill
# -------------------------------
print("\nAverage Bill by Gender\n")
print(df.groupby("Gender")["Bill"].mean())

# -------------------------------
# Disease Summary
# -------------------------------
summary = df.groupby("Disease").agg({
    "Bill":"mean",
    "Age":"mean",
    "BMI":"mean"
})

print("\nDisease Summary\n")
print(summary)

# -------------------------------
# Top 5 Highest Bills
# -------------------------------
top = df.sort_values("Bill",ascending=False).head(5)

print("\nTop Billing Patients\n")
print(top[["Name","Disease","Bill"]])

# -------------------------------
# Pivot Table
# -------------------------------
pivot = pd.pivot_table(
    df,
    values="Bill",
    index="Disease",
    columns="Gender",
    aggfunc="mean",
    fill_value=0
)

print("\nPivot Table\n")
print(pivot)

# -------------------------------
# Statistics
# -------------------------------
print("\nStatistics\n")
print(df.describe())

# -------------------------------
# Export Reports
# -------------------------------
df.to_csv("patients_report.csv",index=False)
summary.to_csv("disease_summary.csv")
pivot.to_csv("bill_pivot.csv")

print("\nAll Reports Saved Successfully!")