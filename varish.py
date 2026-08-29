import json


class TaskManager:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        task = {"id": len(self.tasks) + 1, "title": title, "done": False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added task: '{title}'")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            print(f"[{status}] {task['id']}. {task['title']}")


# Example Usage
manager = TaskManager()
manager.add_task("Learn Python Code")
manager.add_task("Build a mini project")
manager.show_tasks()