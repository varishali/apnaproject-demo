import pandas as pd
import os
from datetime import datetime

FILE = "parking.csv"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Vehicle No", "Owner", "Type", "Entry Time"])
    df.to_csv(FILE, index=False)


def load():
    return pd.read_csv(FILE)


def save(df):
    df.to_csv(FILE, index=False)


while True:
    print("\n===== VEHICLE PARKING SYSTEM =====")
    print("1. Add Vehicle")
    print("2. View Vehicles")
    print("3. Search Vehicle")
    print("4. Delete Vehicle")
    print("5. Count Vehicles")
    print("6. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        no = input("Vehicle Number: ")
        owner = input("Owner Name: ")
        vtype = input("Vehicle Type: ")

        entry = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        df = load()

        new = pd.DataFrame({
            "Vehicle No": [no],
            "Owner": [owner],
            "Type": [vtype],
            "Entry Time": [entry]
        })

        df = pd.concat([df, new], ignore_index=True)
        save(df)

        print("Vehicle Added Successfully!")

    elif ch == "2":
        df = load()

        if df.empty:
            print("No Vehicle Found")
        else:
            print(df.to_string(index=False))

    elif ch == "3":
        df = load()

        no = input("Enter Vehicle Number: ")

        result = df[df["Vehicle No"].str.upper() == no.upper()]

        if result.empty:
            print("Vehicle Not Found")
        else:
            print(result.to_string(index=False))

    elif ch == "4":
        df = load()

        no = input("Vehicle Number To Delete: ")

        df = df[df["Vehicle No"].str.upper() != no.upper()]

        save(df)

        print("Record Deleted Successfully!")

    elif ch == "5":
        df = load()

        print("Total Vehicles:", len(df))

    elif ch == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")