import pandas as pd
data = {
    "Name" : ["varish","ali","sohil"],
    "Marks" : [78,89,67]
}
df = pd.DataFrame(data)

#add new column
df["Result"] = ["pass","fail","pass"]
print(df)
print("\n")
df["City"] = "Dehli"

print(df)
print("\n")

# delete Coloumn
df = df.drop("City",axis=1)
print(df)   

#rename colummn
df = df.rename(columns={"Marks":"Score"})
print(df)   

