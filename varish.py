import pandas as pd

employee_data = {
    "EmpID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Aman","Rahul","Priya","Neha","Arjun","Riya","Karan","Simran","Ankit","Pooja"],
    "Department": ["IT","HR","IT","Sales","HR","IT","Sales","Finance","Finance","IT"],
    "Salary": [55000,42000,65000,45000,50000,70000,48000,60000,58000,62000],
    "Experience": [2,5,4,3,6,5,4,7,3,6],
    "Rating": [4.2,3.8,4.7,4.1,4.5,4.9,3.9,4.8,4.0,4.6]
}

employee_df = pd.DataFrame(employee_data)

# CSV File Create
employee_df.to_csv("employee.csv", index=False)

print("employee.csv file successfully created!")
print(employee_df)