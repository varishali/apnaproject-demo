import pandas as pd

data = {
    "PLAYER": ["Virat", "Rohit", "Gill", "Dhoni"],
    "RUNS": [120, 45, 99, 70],
    "TEAM": ["RCB", "MI", "GT", "CSK"]
}

df = pd.DataFrame(data)

print("Full Data:\n")
print(df)

print("\nSecond Row:\n")
print(df.iloc[1])

print("\nSpecific Value:\n")
print(df.iloc[2, 0])

print("\nFirst Two Rows:\n")
print(df.iloc[0:2])

print("\nRows and Columns Slice:\n")
print(df.iloc[0:3, 0:2])