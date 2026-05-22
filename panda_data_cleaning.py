import pandas as pd

data = {
    "Name" : ["Varish","ali","ali","sohil"],
    "Marks" : [78,None,None,90]
}
df = pd.DataFrame(data)

print("Original Data\n")
print(df)

print("\nMissing Value : \n")
print(df.isnull())

# fill missing values
df["Marks"] = df["Marks"].fillna(89)
print("\nAfter Fillna() : \n")
print(df)

print("\nAfter Removing Duplicate : \n")
print(df.drop_duplicates())