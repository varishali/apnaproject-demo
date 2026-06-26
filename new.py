from collections import Counter

data = ["apple", "Banana", "apple", "orange", "BANANA", "grape"]
clean_data = [word.lower() for word in data if len(word) > 4]
counts = Counter(clean_data)
formatter = lambda k, v: f"{k.title()}: {v} times"
for fruit, count in zip(counts.keys(), counts.values()):
    print(formatter(fruit, count))