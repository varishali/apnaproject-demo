import pandas as pd

# IPL Player Data
data = {
    "PLAYER": ["Virat", "Rohit", "Gill", "Dhoni", "Hardik"],
    "RUNS": [120, 45, 99, 70, 88],
    "TEAM": ["RCB", "MI", "GT", "CSK", "MI"]
}

# DataFrame
df = pd.DataFrame(data)

# Stylish Heading
print("\033[1;96m")
print("=" * 45)
print("           IPL RUNS ANALYZER")
print("=" * 45)
print("\033[0m")

# Full Data
print("\n\033[1;93m[PLAYER DATA]\033[0m\n")
print(df)

# Average Runs
print("\nAverage Runs:")
print(df["RUNS"].mean())

# Highest Runs
print("\nHighest Runs:")
print(df["RUNS"].max())

# Lowest Runs
print("\nLowest Runs:")
print(df["RUNS"].min())

# Total Runs
print("\nTotal Runs:")
print(df["RUNS"].sum())

# Filtering
print("\n\033[1;92mPlayers Scoring More Than 80:\033[0m\n")
print(df[df["RUNS"] > 80])

# Sorting
print("\n\033[1;95mPlayers Sorted By Runs:\033[0m\n")
print(df.sort_values("RUNS", ascending=False))

# iloc Example
print("\n\033[1;94mTop Player Using iloc:\033[0m\n")
print(df.iloc[0])

print("\n" + "=" * 45)
print("           ANALYSIS COMPLETED")
print("=" * 45)