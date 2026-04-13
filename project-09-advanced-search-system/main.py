import json
import os
from typing import List, Dict, Any

FILE_NAME = "records.json"


def load_data() -> List[Dict[str, Any]]:
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_data(data: List[Dict[str, Any]]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


class SearchSystem:
    def __init__(self) -> None:
        self.records = load_data()

    def generate_id(self) -> int:
        if not self.records:
            return 1
        return max(record["id"] for record in self.records) + 1

    def add_record(self) -> None:
        print("\nAdd New Record")
        name = input("Name: ").strip()
        category = input("Category: ").strip()

        try:
            price = float(input("Price: ").strip())
            rating = float(input("Rating (1-5): ").strip())
        except ValueError:
            print("Invalid numeric input.")
            return

        if not name or not category:
            print("Name and category are required.")
            return

        record = {
            "id": self.generate_id(),
            "name": name,
            "category": category,
            "price": price,
            "rating": rating,
        }

        self.records.append(record)
        save_data(self.records)
        print("Record added successfully.")

    def view_all(self) -> None:
        if not self.records:
            print("No records found.")
            return

        print("\nAll Records")
        for record in self.records:
            self.print_record(record)

    def print_record(self, record: Dict[str, Any]) -> None:
        print("-" * 30)
        print(f"ID: {record['id']}")
        print(f"Name: {record['name']}")
        print(f"Category: {record['category']}")
        print(f"Price: {record['price']}")
        print(f"Rating: {record['rating']}")

    def search_by_name(self) -> None:
        keyword = input("Search name: ").strip().lower()
        results = [
            record for record in self.records
            if keyword in record["name"].lower()
        ]

        if not results:
            print("No matching records found.")
            return

        print("\nSearch Results")
        for record in results:
            self.print_record(record)

    def filter_by_category(self) -> None:
        category = input("Category: ").strip().lower()
        results = [
            record for record in self.records
            if record["category"].lower() == category
        ]

        if not results:
            print("No records found in this category.")
            return

        print("\nCategory Filter Results")
        for record in results:
            self.print_record(record)

    def filter_by_price_range(self) -> None:
        try:
            min_price = float(input("Minimum price: ").strip())
            max_price = float(input("Maximum price: ").strip())
        except ValueError:
            print("Invalid numeric input.")
            return

        results = [
            record for record in self.records
            if min_price <= record["price"] <= max_price
        ]

        if not results:
            print("No records found in this price range.")
            return

        print("\nPrice Range Results")
        for record in results:
            self.print_record(record)

    def sort_records(self) -> None:
        print("\nSort Options")
        print("1. Price ascending")
        print("2. Price descending")
        print("3. Rating ascending")
        print("4. Rating descending")
        print("5. Name A-Z")

        choice = input("Choose: ").strip()

        if choice == "1":
            sorted_records = sorted(self.records, key=lambda x: x["price"])
        elif choice == "2":
            sorted_records = sorted(self.records, key=lambda x: x["price"], reverse=True)
        elif choice == "3":
            sorted_records = sorted(self.records, key=lambda x: x["rating"])
        elif choice == "4":
            sorted_records = sorted(self.records, key=lambda x: x["rating"], reverse=True)
        elif choice == "5":
            sorted_records = sorted(self.records, key=lambda x: x["name"].lower())
        else:
            print("Invalid choice.")
            return

        print("\nSorted Results")
        for record in sorted_records:
            self.print_record(record)

    def delete_record(self) -> None:
        try:
            record_id = int(input("Enter ID to delete: ").strip())
        except ValueError:
            print("Invalid ID.")
            return

        for record in self.records:
            if record["id"] == record_id:
                self.records.remove(record)
                save_data(self.records)
                print("Record deleted successfully.")
                return

        print("Record not found.")

    def menu(self) -> None:
        while True:
            print("\n=== Advanced Search System ===")
            print("1. Add Record")
            print("2. View All Records")
            print("3. Search by Name")
            print("4. Filter by Category")
            print("5. Filter by Price Range")
            print("6. Sort Records")
            print("7. Delete Record")
            print("8. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                self.search_by_name()
            elif choice == "4":
                self.filter_by_category()
            elif choice == "5":
                self.filter_by_price_range()
            elif choice == "6":
                self.sort_records()
            elif choice == "7":
                self.delete_record()
            elif choice == "8":
                print("Goodbye.")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    app = SearchSystem()
    app.menu()
