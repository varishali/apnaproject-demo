import time

sentence = "Python is a powerful language"

print(sentence)

start = time.time()

typed = input("Type Here: ")

end = time.time()

print("Time Taken:", round(end - start, 2), "seconds")