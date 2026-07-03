# Time module
import time


# Start message
input("Press Enter To Start Stopwatch")


# Start time
start = time.time()


# Stop message
input("Press Enter To Stop Stopwatch")


# End time
end = time.time()


# Total time
total = end - start


# Output
print(f"Time Taken : {total:.2f} Seconds")
                    