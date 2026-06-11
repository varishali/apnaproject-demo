# import pandas as pd

# # student data

# data = {
#     "NAME" : ["Varish","Sohil","Zainul","Ali","Aman"],
#     "MARKS" : [78,45,92,66,88]
# }

# # data frame
# df = pd.DataFrame(data)
# print("\033[1;92m")
# print("=" *33)
# print("     STUDENT RESULT ANALYZER")
# print("=" *33)
# print("\033[0m")

# # full bdata
# print("\n\033[;93m[Full Student Data]\033[0m\n")
# print(df)

# # average marks
# print("\n\033[1;96mAverage Marks : \033[0m")
# print(df["MARKS"].mean())

# # highest marks
# print("\n\033[1;96mHighest Marks : \033[0m")
# print(df["MARKS"].max())

# # Lowest marks
# print("\033[1;96m\nLowest Marks : \033[0m")
# print(df["MARKS"].min())

# # total marks
# print("\n\033[1;96mTotal Marks : \033[0m")
# print(df["MARKS"].sum())

# # passed students
# print("\n\033[1;96mStudent Scoring more than 70 : \033[0m\n")
# print(df[df["MARKS"] >= 70])

# # stored data 
# print("\n\033[1;96mStudent Stored By Marks : \033[0m\n")
# print(df.sort_values("MARKS",ascending=False))

# print("\033[;95m")
# print("\n" + "=" *27)
# print("     Analyze Completed")
# print("=" *27)
# print("\033[0m")
