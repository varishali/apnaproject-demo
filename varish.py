import time
seconds = int(input("Enter Seconds : "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1
print("Time Up!")