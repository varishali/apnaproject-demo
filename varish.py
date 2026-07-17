import pandas as pd

# read CSV file
df = pd.read_csv("file.csv")

print("\n\033[1;103m==========================  STUDENTS RESULT ANALYZER  ==========================\033[0m\n")

print("\n\033[1;102m--------------   STUDENT DATA  ------------------\033[0m\n")
print("\033[0;91m",df,"\033[0m")


# total marks
df["Total"] = df["Math"] + df["Science"] + df["English"]

# average marks
df["Average"] = df["Total"] / 3


# result
df["Result"] = df["Average"].apply(lambda x: "Pass" if x>=40 else "Fail")


# grade

def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)


# show update data 
print("\n\033[1;102m----------------------------------- RESULT ------------------------------------\033[0m\n")
print("\033[0;91m",df,"\033[0m")    