# REST API with Database

A Flask backend project using SQLite for persistent data storage.

---

## Overview

This project demonstrates how to build a REST API connected to a database using Flask and SQLite.

---

## Features

- Create records
- Get all records
- Get record by ID
- Update records
- Delete records
- Persistent storage using SQLite

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- README.md → Documentation

---

## Endpoints

### Get all items
GET /items

### Get item by ID
GET /items/<id>

### Create item
POST /items

### Update item
PUT /items/<id>

### Delete item
DELETE /items/<id>

---

## Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON

---

## Run the Project

```bash
pip install -r requirements.txt
python app.py

---

## Example JSON

{
  "name": "Laptop",
  "price": 1200
}

-----------------
Author

Alhanoof Alabdullah
