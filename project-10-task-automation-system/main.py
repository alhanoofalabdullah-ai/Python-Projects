import json
import os
from datetime import datetime
from typing import List, Dict, Optional


TASKS_FILE = "tasks.json"
LOG_FILE = "activity_log.txt"


class TaskAutomationSystem:
    def __init__(self) -> None:
        self.tasks: List[Dict] = self.load_tasks()

    # =========================
    # File Handling
    # =========================
    def load_tasks(self) -> List[Dict]:
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r", encoding="utf-8") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self) -> None:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)

    def log_action(self, action: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {action}\n")

    # =========================
    # Utility Methods
    # =========================
    def generate_task_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def get_task_by_id(self, task_id: int) -> Optional[Dict]:
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def validate_priority(self, value: str) -> bool:
        return value.lower() in ["low", "medium", "high", "critical"]

    def validate_status(self, value: str) -> bool:
        return value.lower() in ["pending", "in progress", "completed", "cancelled"]

    def validate_date(self, value: str) -> bool:
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def print_task(self, task: Dict) -> None:
        print("-" * 50)
        print(f"ID           : {task['id']}")
        print(f"Title        : {task['title']}")
        print(f"Description  : {task['description']}")
        print(f"Assigned To  : {task['assigned_to']}")
        print(f"Priority     : {task['priority']}")
        print(f"Status       : {task['status']}")
        print(f"Due Date     : {task['due_date']}")
        print(f"Created At   : {task['created_at']}")
        print(f"Updated At   : {task['updated_at']}")

    # =========================
    # CRUD Operations
    # =========================
    def add_task(self) -> None:
        print("\nAdd New Task")
        title = input("Title: ").strip()
        description = input("Description: ").strip()
        assigned_to = input("Assigned to: ").strip()

        priority = input("Priority (Low / Medium / High / Critical): ").strip().lower()
        if not self.validate_priority(priority):
            print("Invalid priority.")
            return

        status = input("Status (Pending / In Progress / Completed / Cancelled): ").strip().lower()
        if not self.validate_status(status):
            print("Invalid status.")
            return

        due_date = input("Due date (YYYY-MM-DD): ").strip()
        if not self.validate_date(due_date):
            print("Invalid date format.")
            return

        if not title:
            print("Task title is required.")
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        task = {
            "id": self.generate_task_id(),
            "title": title,
            "description": description,
            "assigned_to": assigned_to,
            "priority": priority.title(),
            "status": status.title(),
            "due_date": due_date,
            "created_at": now,
            "updated_at": now,
        }

        self.tasks.append(task)
        self.save_tasks()
        self.log_action(f"Added task ID {task['id']} - {title}")
        print("Task added successfully.")

    def view_all_tasks(self) -> None:
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nAll Tasks")
        for task in self.tasks:
            self.print_task(task)

    def update_task(self) -> None:
        try:
            task_id = int(input("Enter task ID to update: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        task = self.get_task_by_id(task_id)
        if not task:
            print("Task not found.")
            return

        print("Leave field blank to keep current value.")

        title = input(f"Title [{task['title']}]: ").strip()
        description = input(f"Description [{task['description']}]: ").strip()
        assigned_to = input(f"Assigned To [{task['assigned_to']}]: ").strip()
        priority = input(f"Priority [{task['priority']}]: ").strip()
        status = input(f"Status [{task['status']}]: ").strip()
        due_date = input(f"Due Date [{task['due_date']}]: ").strip()

        if title:
            task["title"] = title
        if description:
            task["description"] = description
        if assigned_to:
            task["assigned_to"] = assigned_to

        if priority:
            if not self.validate_priority(priority):
                print("Invalid priority.")
                return
            task["priority"] = priority.title()

        if status:
            if not self.validate_status(status):
                print("Invalid status.")
                return
            task["status"] = status.title()

        if due_date:
            if not self.validate_date(due_date):
                print("Invalid date format.")
                return
            task["due_date"] = due_date

        task["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_tasks()
        self.log_action(f"Updated task ID {task_id}")
        print("Task updated successfully.")

    def delete_task(self) -> None:
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        task = self.get_task_by_id(task_id)
        if not task:
            print("Task not found.")
            return

        self.tasks.remove(task)
        self.save_tasks()
        self.log_action(f"Deleted task ID {task_id}")
        print("Task deleted successfully.")

    # =========================
    # Search and Filter
    # =========================
    def search_tasks(self) -> None:
        keyword = input("Search keyword (title / description / assigned to): ").strip().lower()

        results = [
            task for task in self.tasks
            if keyword in task["title"].lower()
            or keyword in task["description"].lower()
            or keyword in task["assigned_to"].lower()
        ]

        if not results:
            print("No matching tasks found.")
            return

        print("\nSearch Results")
        for task in results:
            self.print_task(task)

    def filter_by_status(self) -> None:
        status = input("Filter by status: ").strip().lower()

        results = [task for task in self.tasks if task["status"].lower() == status]

        if not results:
            print("No tasks found for this status.")
            return

        print("\nFiltered by Status")
        for task in results:
            self.print_task(task)

    def filter_by_priority(self) -> None:
        priority = input("Filter by priority: ").strip().lower()

        results = [task for task in self.tasks if task["priority"].lower() == priority]

        if not results:
            print("No tasks found for this priority.")
            return

        print("\nFiltered by Priority")
        for task in results:
            self.print_task(task)

    def filter_overdue_tasks(self) -> None:
        today = datetime.now().date()
        results = []

        for task in self.tasks:
            try:
                due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
                if due_date < today and task["status"].lower() != "completed":
                    results.append(task)
            except ValueError:
                continue

        if not results:
            print("No overdue tasks found.")
            return

        print("\nOverdue Tasks")
        for task in results:
            self.print_task(task)

    # =========================
    # Sorting
    # =========================
    def sort_tasks(self) -> None:
        print("\nSort Options")
        print("1. Due Date Ascending")
        print("2. Due Date Descending")
        print("3. Priority")
        print("4. Title A-Z")
        print("5. Created Date Descending")

        choice = input("Choose sort option: ").strip()

        priority_order = {
            "Low": 1,
            "Medium": 2,
            "High": 3,
            "Critical": 4
        }

        if choice == "1":
            sorted_tasks = sorted(self.tasks, key=lambda t: t["due_date"])
        elif choice == "2":
            sorted_tasks = sorted(self.tasks, key=lambda t: t["due_date"], reverse=True)
        elif choice == "3":
            sorted_tasks = sorted(self.tasks, key=lambda t: priority_order.get(t["priority"], 0), reverse=True)
        elif choice == "4":
            sorted_tasks = sorted(self.tasks, key=lambda t: t["title"].lower())
        elif choice == "5":
            sorted_tasks = sorted(self.tasks, key=lambda t: t["created_at"], reverse=True)
        else:
            print("Invalid option.")
            return

        print("\nSorted Tasks")
        for task in sorted_tasks:
            self.print_task(task)

    # =========================
    # Reports and Dashboard
    # =========================
    def dashboard(self) -> None:
        total_tasks = len(self.tasks)
        pending_tasks = sum(1 for t in self.tasks if t["status"].lower() == "pending")
        in_progress_tasks = sum(1 for t in self.tasks if t["status"].lower() == "in progress")
        completed_tasks = sum(1 for t in self.tasks if t["status"].lower() == "completed")
        cancelled_tasks = sum(1 for t in self.tasks if t["status"].lower() == "cancelled")
        critical_tasks = sum(1 for t in self.tasks if t["priority"].lower() == "critical")

        print("\nTask Dashboard")
        print("-" * 30)
        print(f"Total Tasks      : {total_tasks}")
        print(f"Pending          : {pending_tasks}")
        print(f"In Progress      : {in_progress_tasks}")
        print(f"Completed        : {completed_tasks}")
        print(f"Cancelled        : {cancelled_tasks}")
        print(f"Critical Tasks   : {critical_tasks}")

    def assigned_tasks_report(self) -> None:
        summary = {}

        for task in self.tasks:
            person = task["assigned_to"] if task["assigned_to"] else "Unassigned"
            summary[person] = summary.get(person, 0) + 1

        if not summary:
            print("No task assignment data found.")
            return

        print("\nTasks by Assignee")
        print("-" * 30)
        for assignee, count in summary.items():
            print(f"{assignee}: {count}")

    def status_report(self) -> None:
        summary = {}

        for task in self.tasks:
            status = task["status"]
            summary[status] = summary.get(status, 0) + 1

        if not summary:
            print("No status data found.")
            return

        print("\nTasks by Status")
        print("-" * 30)
        for status, count in summary.items():
            print(f"{status}: {count}")

    # =========================
    # Menu
    # =========================
    def menu(self) -> None:
        while True:
            print("\n" + "=" * 60)
            print("Task Automation System Pro")
            print("=" * 60)
            print("1.  Add Task")
            print("2.  View All Tasks")
            print("3.  Update Task")
            print("4.  Delete Task")
            print("5.  Search Tasks")
            print("6.  Filter by Status")
            print("7.  Filter by Priority")
            print("8.  Show Overdue Tasks")
            print("9.  Sort Tasks")
            print("10. Dashboard")
            print("11. Assigned Tasks Report")
            print("12. Status Report")
            print("13. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.search_tasks()
            elif choice == "6":
                self.filter_by_status()
            elif choice == "7":
                self.filter_by_priority()
            elif choice == "8":
                self.filter_overdue_tasks()
            elif choice == "9":
                self.sort_tasks()
            elif choice == "10":
                self.dashboard()
            elif choice == "11":
                self.assigned_tasks_report()
            elif choice == "12":
                self.status_report()
            elif choice == "13":
                print("Exiting Task Automation System. Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = TaskAutomationSystem()
    app.menu()
