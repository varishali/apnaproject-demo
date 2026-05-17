import time 

print("\033[1m==========================")
print("|  DIGITAL CLOCK SYSTEM  |")
print("==========================\033[0m")

current_time = time.localtime()
formatted_time = time.strftime ("Date : %Y/%m/%d \nTime : %I:%M:%S %p")
print(formatted_time)

print("\033[1m\nClock loaded Successfully!\033[0m")