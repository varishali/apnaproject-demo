import pandas as pd
import os
from datetime import datetime

FILE = "history.csv"

# Create CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "News", "Score", "Result"])
    df.to_csv(FILE, index=False)

fake_keywords = [
    "free", "click", "win", "urgent", "money",
    "offer", "lottery", "guaranteed", "virus",
    "hack", "breaking", "limited", "prize"
]

def analyze_news(news):
    score = 0
    matched = []

    text = news.lower()

    for word in fake_keywords:
        if word in text:
            score += 8
            matched.append(word)

    score = min(score, 100)

    if score >= 60:
        result = "Highly Fake"
    elif score >= 30:
        result = "Suspicious"
    else:
        result = "Likely Real"

    return score, result, matched


while True:
    print("\n====== FAKE NEWS DETECTOR ======")
    print("1. Analyze News")
    print("2. View History")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        news = input("\nPaste News:\n")

        score, result, matched = analyze_news(news)

        print("\nScore :", score, "%")
        print("Result :", result)

        if matched:
            print("Matched Keywords:", ", ".join(matched))
        else:
            print("No Suspicious Keywords Found.")

        df = pd.read_csv(FILE)

        new = pd.DataFrame({
            "Date": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "News": [news],
            "Score": [score],
            "Result": [result]
        })

        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(FILE, index=False)

    elif choice == "2":
        df = pd.read_csv(FILE)

        if df.empty:
            print("\nNo History Found.")
        else:
            print("\n===== HISTORY =====")
            print(df.to_string(index=False))

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")