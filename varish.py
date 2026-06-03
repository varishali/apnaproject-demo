tasks = []

while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        task = input("Enter Task: ")
        tasks.append(task)

        print("Task Added Successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Found!")

        else:
            print("\nTasks:")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks To Remove!")

        else:

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter Task Number: "))
                removed_task = tasks.pop(index - 1)

                print(f"{removed_task} Removed Successfully!")

            except:
                print("Invalid Task Number!")

    elif choice == "4":

        print("Thanks For Using To-Do List!")
        break

    else:

        print("Invalid Choice!")
