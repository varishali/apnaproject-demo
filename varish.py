import time

text = "python"

start = time.time()

user = input("Type Word : ")

end = time.time()

print("Time :", end - start)

if user == text:

    print("Correct")