import pandas as pd
data = {
    "Name" : ["Varish","Ali","Aman","Sohil","Zainul"],
    "Marks" : [89,90,45,67,78]
}

# DATA FRAME
df = pd.DataFrame(data)

# EMPTY LIST
result = []

for marks in df["Marks"]:
    if marks >= 50:
        result.append("Pass")

    else:
        result.append("Fail")

# ADD NEW COLLUMN
df["Result"] = result

# FULL DATA
print("=" *40)
print("         Student Pass Fail Analyzer")
print("=" *40)

print("\nStudnet Data :\n")
print(df)





