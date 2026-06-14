from datetime import datetime

birth_date = input("Enter Date of Birth (DD/MM/YYYY): ")

dob = datetime.strptime(birth_date, "%d/%m/%Y")

today = datetime.now()

years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day

if days < 0:
    months -= 1
    days += 30

if months < 0:
    years -= 1
    months += 12

print("\n===== AGE DETAILS =====")
print(f"Years  : {years}")
print(f"Months : {months}")
print(f"Days   : {days}")