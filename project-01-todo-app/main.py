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
        json.dump(tasks, file)

tasks = load_tasks()

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if num < 1 or num > len(tasks):
            print("Task number does not exist")
            return
        removed = tasks.pop(num-1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    except:
        print("Invalid input")

def menu():
    while True:
        print("\n--- To-Do App ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()
