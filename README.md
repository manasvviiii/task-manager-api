# Task Manager REST API

A backend REST API for managing tasks built with FastAPI and PostgreSQL.

## Features

- User registration and login
- JWT authentication
- CRUD operations for tasks
- PostgreSQL database
- SQLAlchemy ORM
- Interactive API docs with Swagger

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Passlib (password hashing)

## API Endpoints

POST /register  
POST /login  
POST /tasks  
GET /tasks  
PUT /tasks/{task_id}  
DELETE /tasks/{task_id}

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
