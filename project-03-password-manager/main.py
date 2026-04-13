import json
import os

FILE_NAME = "passwords.json"


def load_passwords():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_passwords(passwords):
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file)


passwords = load_passwords()


def show_passwords():
    if not passwords:
        print("No saved accounts yet.")
    else:
        print("\nSaved Accounts:")
        for i, item in enumerate(passwords):
            print(f"{i+1}. Website: {item['website']} | Username: {item['username']} | Password: {item['password']}")


def add_password():
    website = input("Website name: ")
    username = input("Username: ")
    password = input("Password: ")
    passwords.append({
        "website": website,
        "username": username,
        "password": password
    })
    save_passwords(passwords)
    print("Account saved successfully!")


def delete_password():
    show_passwords()
    try:
        num = int(input("Enter account number to delete: "))
        if num < 1 or num > len(passwords):
            print("Account number does not exist")
            return
        removed = passwords.pop(num - 1)
        save_passwords(passwords)
        print(f"Removed account for {removed['website']}")
    except:
        print("Invalid input")


def menu():
    while True:
        print("\n--- Password Manager ---")
        print("1. Show Accounts")
        print("2. Add Account")
        print("3. Delete Account")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_passwords()
        elif choice == "2":
            add_password()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


menu()
