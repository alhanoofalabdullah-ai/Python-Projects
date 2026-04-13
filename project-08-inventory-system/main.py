import json
import os
from datetime import datetime

FILE_NAME = "inventory.json"


# =========================
# File Handling
# =========================
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def log_action(action):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {action}")


# =========================
# Product Class
# =========================
class Product:
    def __init__(self, id, name, quantity, price, category):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category
        }


# =========================
# Inventory System
# =========================
class InventorySystem:
    def __init__(self):
        self.products = load_data()

    def generate_id(self):
        if not self.products:
            return 1
        return max(p["id"] for p in self.products) + 1

    def add_product(self):
        name = input("Product name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))
        category = input("Category: ")

        product = Product(
            self.generate_id(),
            name,
            quantity,
            price,
            category
        )

        self.products.append(product.to_dict())
        save_data(self.products)
        log_action(f"Added product: {name}")

    def view_products(self):
        if not self.products:
            print("No products found.")
            return

        for p in self.products:
            print(p)

    def search_product(self):
        keyword = input("Search by name or category: ").lower()

        results = [
            p for p in self.products
            if keyword in p["name"].lower()
            or keyword in p["category"].lower()
        ]

        for r in results:
            print(r)

    def update_product(self):
        id = int(input("Enter product ID: "))

        for p in self.products:
            if p["id"] == id:
                p["name"] = input("New name: ")
                p["quantity"] = int(input("New quantity: "))
                p["price"] = float(input("New price: "))
                p["category"] = input("New category: ")

                save_data(self.products)
                log_action(f"Updated product ID: {id}")
                return

        print("Product not found.")

    def delete_product(self):
        id = int(input("Enter product ID: "))

        self.products = [p for p in self.products if p["id"] != id]
        save_data(self.products)
        log_action(f"Deleted product ID: {id}")

    def report(self):
        total_value = sum(p["quantity"] * p["price"] for p in self.products)
        print(f"Total Inventory Value: {total_value}")


# =========================
# Main Menu
# =========================
def main():
    system = InventorySystem()

    while True:
        print("\n--- Inventory System ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Report")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            system.add_product()
        elif choice == "2":
            system.view_products()
        elif choice == "3":
            system.search_product()
        elif choice == "4":
            system.update_product()
        elif choice == "5":
            system.delete_product()
        elif choice == "6":
            system.report()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
