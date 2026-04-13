import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# =========================
# Helper Functions
# =========================
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def log_action(action):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action}")


# =========================
# Task Class
# =========================
class Task:
    def __init__(self, id, title, priority, status, due_date):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status
        self.due_date = due_date

    def to_dict(self):
        return self.__dict__


# =========================
# Task System
# =========================
class TaskSystem:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self):
        title = input("Task title: ")
        priority = input("Priority (High/Medium/Low): ")
        due_date = input("Due date (YYYY-MM-DD): ")

        task = Task(
            id=len(self.tasks) + 1,
            title=title,
            priority=priority,
            status="Pending",
            due_date=due_date
        )

        self.tasks.append(task.to_dict())
        save_tasks(self.tasks)
        log_action("Task added successfully")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found")
            return

        for task in self.tasks:
            print(task)

    def delete_task(self):
        task_id = int(input("Enter task ID: "))
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        save_tasks(self.tasks)
        log_action("Task deleted")

    def update_status(self):
        task_id = int(input("Enter task ID: "))
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = input("New status: ")
        save_tasks(self.tasks)
        log_action("Task updated")

    def filter_tasks(self):
        priority = input("Filter by priority: ")
        filtered = [t for t in self.tasks if t["priority"] == priority]

        for task in filtered:
            print(task)

    def overdue_tasks(self):
        today = datetime.now().date()
        for task in self.tasks:
            due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            if due < today:
                print(task)

    def dashboard(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["status"] == "Done"])
        pending = total - completed

        print(f"Total: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")


# =========================
# Main CLI
# =========================
def main():
    system = TaskSystem()

    while True:
        print("\n--- Task Automation System ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Update Status")
        print("5. Filter Tasks")
        print("6. Overdue Tasks")
        print("7. Dashboard")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            system.add_task()
        elif choice == "2":
            system.view_tasks()
        elif choice == "3":
            system.delete_task()
        elif choice == "4":
            system.update_status()
        elif choice == "5":
            system.filter_tasks()
        elif choice == "6":
            system.overdue_tasks()
        elif choice == "7":
            system.dashboard()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
