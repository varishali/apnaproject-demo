
import time 
t = time.localtime()
formatted_time = time.strftime (f"Date = {"%Y/%m/%d"} | time = {"%I:%M:%S %p"}")
print(formatted_time)