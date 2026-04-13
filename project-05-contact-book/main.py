import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


def show_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact['name']} | {contact['phone']} | {contact['email']}")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!")


def search_contact():
    keyword = input("Enter name to search: ").lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"Found: {contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("No matching contact found.")


def delete_contact():
    show_contacts()
    try:
        num = int(input("Enter contact number to delete: "))
        if num < 1 or num > len(contacts):
            print("Contact number does not exist.")
            return

        removed = contacts.pop(num - 1)
        save_contacts(contacts)
        print(f"Deleted: {removed['name']}")
    except:
        print("Invalid input")


def menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


menu()
