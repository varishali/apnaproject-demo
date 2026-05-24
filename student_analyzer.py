import pandas as pd
data = {
    "Name" : ["varish","sohil","zainul","aman","ali"],
    "Marks" : [89,56,78,90,95],
    "City" : ["Dehli","Noida","Dehli","Lucknow","Noida"]
}

df = pd.DataFrame(data)
print("\033[1;92m") 
print("=" *45)
print("         STUDENT RESULT ANALYZER")
print("=" *45)
print("\033[0m")
print("\033[;93m[Student Data]\033[0m\n")
# full data
print(df)

# statistic

print("\nAverage Marks :")
print(df["Marks"].mean())

print("\nHighest Marks :")
print(df["Marks"].max())

print("\nLowest Marks :")
print(df["Marks"].min())

# filtering
print("\n\033[1;93mStudent scoring more than 70 :\033[0m")
print(df[df["Marks"] > 70])

# sorting
print("\n\033[1;93mStudent sorted by marks :\033[0m\n")
print(df.sort_values("Marks",ascending=False))

print("\n" + "=" *45)
print("            ANALYZE COMPLETE")
print("=" *45)






