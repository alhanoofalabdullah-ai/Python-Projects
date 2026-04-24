# Advanced API with Auth and JWT

A Flask backend project implementing user authentication with JWT.

---

## Overview

This project demonstrates how to build a secure API using Flask with user registration, login, and JWT-protected routes.

---

## Features

- User registration
- User login
- Password hashing
- JWT token generation
- Protected route access
- SQLite database integration

---

## Project Structure

- app.py → Flask application
- requirements.txt → Project dependencies
- database.db → SQLite database
- README.md → Documentation

---

## Endpoints

### Register user
POST /register

### Login user
POST /login

### Protected route
GET /protected

---

## Technologies Used

- Python
- Flask
- SQLite
- JWT
- Password Hashing
- REST API

---

## Run the Project

```bash
pip install -r requirements.txt
python app.py

## Example JSON
Register / Login

{
  "username": "alhanoof",
  "password": "123456"
}

## Setup Commands

- cd ~/Python-Projects
- mkdir project-17-advanced-api-jwt
- cd project-17-advanced-api-jwt
- touch README.md app.py requirements.txt

## Run

- pip install -r requirements.txt
- python app.py

## Git

- cd ..
- git add .
- git commit -m "add project 17 advanced api jwt"
- git push

## API testing

- POST http://127.0.0.1:5000/register
- POST http://127.0.0.1:5000/login
- GET http://127.0.0.1:5000/protected

## protected / header

Authorization: Bearer YOUR_TOKEN

---------------
Author

Alhanoof Alabdullah
