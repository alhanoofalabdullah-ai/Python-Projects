import json
import os

FILE_NAME = "data.json"

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

students = load_data()

# =========================
# Student Class
# =========================
class Student:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major
        self.grades = []

    def to_dict(self):
        return self.__dict__

# =========================
# Utility Functions
# =========================
def generate_id():
    return max([s["id"] for s in students], default=0) + 1

def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

# =========================
# Core Features
# =========================
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")

    student = Student(generate_id(), name, age, major)
    students.append(student.to_dict())
    save_data(students)

    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Major: {s['major']}")

def delete_student():
    student_id = int(input("Enter student ID: "))
    student = find_student(student_id)

    if student:
        students.remove(student)
        save_data(students)
        print("🗑️ Student deleted.")
    else:
        print("❌ Student not found.")

def add_grade():
    student_id = int(input("Enter student ID: "))
    student = find_student(student_id)

    if student:
        grade = float(input("Enter grade: "))
        student["grades"].append(grade)
        save_data(students)
        print("📊 Grade added.")
    else:
        print("❌ Student not found.")

def calculate_average():
    student_id = int(input("Enter student ID: "))
    student = find_student(student_id)

    if student and student["grades"]:
        avg = sum(student["grades"]) / len(student["grades"])
        print(f"📈 Average: {avg:.2f}")
    else:
        print("❌ No grades found.")

# =========================
# Menu
# =========================
def menu():
    while True:
        print("\n=== 🎓 Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Add Grade")
        print("5. Calculate Average")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            add_grade()
        elif choice == "5":
            calculate_average()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice!")

# =========================
# Run
# =========================
if __name__ == "__main__":
    menu()
