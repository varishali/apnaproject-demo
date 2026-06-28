from datetime import datetime


class NotesManager:

    def __init__(self, filename):

        self.filename = filename


    def save_note(self, note):

        time = datetime.now()


        with open(self.filename, "a") as file:

            file.write(f"{time} -> {note}\n")


        print("Note Saved Successfully!")


notes = NotesManager("notes.txt")


while True:

    note = input("Write Note : ")


    if note == "exit":

        print("Program Closed")

        break


    notes.save_note(note)


