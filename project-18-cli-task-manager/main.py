
## main.py

```python
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_menu():
    print("\nTask Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete task")
    print("6. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully.")


def update_task(tasks):
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            new_title = input("Enter new task title: ").strip()

            if not new_title:
                print("Task title cannot be empty.")
                return

            task["title"] = new_title
            save_tasks(tasks)
            print("Task updated successfully.")
            return

    print("Task not found.")


def complete_task(tasks):
    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
            return

    print("Task not found.")


def delete_task(tasks):
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            for index, item in enumerate(tasks, start=1):
                item["id"] = index

            save_tasks(tasks)
            print("Task deleted successfully.")
            return

    print("Task not found.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
