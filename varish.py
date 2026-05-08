# kon kbanega krorepati (KBC) game in Python

print("====Welcome to kon banega krorepati====")
print(" ====sahi jabab do aur paisa jeeto====\n")

question = [
    {
        "question": "1. who is the first prime minister uof India?" ,
        "option": ["a. Jabahrlal naehru","b. lal bahadur shastri","c. rajiv gandhi","d. Indra gandhi"],
        "answer": "a",
        "money": 1000
    },
    {
        "question": "2. Python kiya hai?",
        "option": ["a. snake","b. programming language","c. game","d. browser"],
        "answer": "b",
        "money": 5000
    },
    {
        "question": "3. what is capital of India?",
        "option": ["a. mumbai","b. bareilly","c. dehli","d. pune"],
        "answer": "c",
        "money": 10000
    },
    {
        "question": "4. which planet is known as the red planet?",
        "option": ["a.Earth","b. venus","c. mars","d. jupiter"],
        "answer": "c",
        "money": 20000
    }
]

total_money = 0


for q in question:
    print(q["question"])

    for option in q["option"]:
        print(option)

    user_answer = input("apna answer likho (a/b/c/d): ")

    if user_answer == q["answer"]:
        total_money = q["money"]
        print("sahi jabab")
        print("aap jeete:",total_money,"rupees\n")

    else:
        print("galat jabab")
        print("game over")
        break
print("\nFinal winning amount : ",total_money,"rupees")        
















