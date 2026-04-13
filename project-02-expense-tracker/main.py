import json
import os

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

expenses = load_expenses()

def show_expenses():
    if not expenses:
        print("No expenses yet.")
    else:
        print("\nExpenses:")
        total = 0
        for i, exp in enumerate(expenses):
            print(f"{i+1}. {exp['name']} - {exp['amount']} SAR")
            total += exp["amount"]
        print(f"\nTotal: {total} SAR")

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    expenses.append({"name": name, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")

def delete_expense():
    show_expenses()
    try:
        num = int(input("Enter number to delete: "))
        removed = expenses.pop(num-1)
        save_expenses(expenses)
        print(f"Removed: {removed['name']}")
    except:
        print("Invalid input")

def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Show Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()
