import time 
alarm_time = input("Set Alarm Time (HH:MM:SS):")
print("Alarm Set For",alarm_time)

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

    if current_time == alarm_time:
        print("Wake Up!")
        break
    time.sleep(1)
