import pandas as pd
data = {
    "Name" : ["Varish","Zainul","Ali","Sohil"],
    "Math_number" : [89,78,90,76,],
    "Physics_number" : [78,98,92,45,],
    "City" : ["Dehli","Mumbai","Lucknow","Dehli"]
}
df = pd.DataFrame(data)
print(df)