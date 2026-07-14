class Alarm:
    def __init__(self, time, label):
        self.time = time
        self.label = label

    def display(self):
        print(f"Time : {self.time}")
        print(f"Label: {self.label}")
        print("-" * 20)


class AlarmManager:
    def __init__(self):
        self.alarms = []

    def add_alarm(self):
        time = input("Enter Alarm Time (HH:MM): ")
        label = input("Enter Alarm Label: ")

        alarm = Alarm(time, label)
        self.alarms.append(alarm)

        print("Alarm Added Successfully!")

    def view_alarms(self):
        if not self.alarms:
            print("No Alarms Found!")
            return

        print("\n----- Alarm List -----")
        for alarm in self.alarms:
            alarm.display()

    def delete_alarm(self):
        time = input("Enter Alarm Time to Delete: ")

        for alarm in self.alarms:
            if alarm.time == time:
                self.alarms.remove(alarm)
                print("Alarm Deleted Successfully!")
                return

        print("Alarm Not Found")


manager = AlarmManager()

while True:
    print("\n===== ALARM MANAGER =====")
    print("1. Add Alarm")
    print("2. View Alarms")
    print("3. Delete Alarm")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        manager.add_alarm()

    elif choice == "2":
        manager.view_alarms()

    elif choice == "3":
        manager.delete_alarm()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")