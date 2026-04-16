from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
FILE_NAME = "tasks.json"


# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())


# Add new task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "status": "pending"
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


# Update task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = request.json.get("status", task["status"])
            save_tasks(tasks)
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


# Delete task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)
