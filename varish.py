from datetime import datetime


class Logger:

    def __init__(self, filename):

        self.filename = filename


    def write_log(self, message):

        time = datetime.now()

        with open(self.filename, "a") as file:

            file.write(f"{time} -> {message}\n")


logger = Logger("log.txt")


while True:

    text = input("Enter Message : ")


    if text == "exit":

        print("Logger Closed")

        break


    logger.write_log(text)

    print("Message Saved")