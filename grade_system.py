import pandas as pd
data = {
    "Marks" : [90,56,45,77,89,92]
}
df = pd.DataFrame(data)

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks < 50:
        return "Fail"
    else:
        return "D"
    

# apply function
df["Grade"] = df["Marks"].apply(grade)

print(df)