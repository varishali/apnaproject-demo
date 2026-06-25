text = input("Enter Sentence : ")

words = len(text.split())

vowels = 0


for ch in text.lower():

    if ch in "aeiou":

        vowels += 1


print("Total Words :", words)

print("Total Vowels :", vowels)

