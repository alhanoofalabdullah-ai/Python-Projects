
---

## 🧠 app.py

```python
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE = "database.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/items", methods=["GET"])
def get_items():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()

    items = [{"id": r[0], "name": r[1], "price": r[2]} for r in rows]
    return jsonify(items), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({"id": row[0], "name": row[1], "price": row[2]}), 200

    return jsonify({"error": "Item not found"}), 404


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    price = data.get("price")

    if not name or price is None:
        return jsonify({"error": "Name and price are required"}), 400

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()

    return jsonify({
        "message": "Item created",
        "item": {"id": item_id, "name": name, "price": price}
    }), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
    if not cursor.fetchone():
        return jsonify({"error": "Item not found"}), 404

    cursor.execute(
        "UPDATE items SET name=?, price=? WHERE id=?",
        (data.get("name"), data.get("price"), item_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Item updated"}), 200


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
    if not cursor.fetchone():
        return jsonify({"error": "Item not found"}), 404

    cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Item deleted"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
