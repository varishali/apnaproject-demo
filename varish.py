import pandas as pd

# ------------------------------
# Create Sample CSV
# ------------------------------

data = {
    "Movie": [
        "KGF 2", "Jawan", "Pathaan", "Animal",
        "Pushpa", "Leo", "RRR", "Dunki",
        "Kalki", "Salaar"
    ],
    "Genre": [
        "Action", "Action", "Action", "Action",
        "Action", "Action", "Drama", "Comedy",
        "Sci-Fi", "Action"
    ],
    "Rating": [
        8.7, 8.1, 7.4, 8.4,
        7.9, 8.3, 8.8, 7.2,
        9.0, 8.6
    ],
    "Votes": [
        120000, 95000, 85000, 110000,
        90000, 98000, 130000, 65000,
        150000, 140000
    ]
}

df = pd.DataFrame(data)
df.to_csv("movies.csv", index=False)

# ------------------------------
# Read CSV
# ------------------------------

df = pd.read_csv("movies.csv")

print("\n===== MOVIE DATA =====")
print(df)

# ------------------------------
# Basic Analysis
# ------------------------------

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nHighest Rated Movie:")
print(df.loc[df["Rating"].idxmax()])

print("\nLowest Rated Movie:")
print(df.loc[df["Rating"].idxmin()])

print("\nTop 5 Movies:")
print(df.sort_values(by="Rating", ascending=False).head())

print("\nGenre Count:")
print(df["Genre"].value_counts())

print("\nMovies with Rating Above 8:")
print(df[df["Rating"] > 8])

print("\nAverage Rating By Genre:")
print(df.groupby("Genre")["Rating"].mean())

print("\nTotal Votes:")
print(df["Votes"].sum())

print("\nTop Voted Movie:")
print(df.sort_values(by="Votes", ascending=False).head(1))

print("\nAnalysis Completed Successfully!")