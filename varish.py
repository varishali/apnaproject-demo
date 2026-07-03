# Time module
import time


# Alarm input
alarm_time = input("Set Alarm Time (HH:MM:SS) : ")


while True:


    # Current time
    current_time = time.strftime("%H:%M:%S")


    print("Current Time :", current_time)


    # Alarm match
    if current_time == alarm_time:


        print("WAKE UP !!!")


        break


    # 1 second wait
    time.sleep(1)
                    