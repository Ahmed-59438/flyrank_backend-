# FlyRank Task 2 – FastAPI Student Management API with PostgreSQL & Docker

## Overview

This project is a RESTful Student Management API built using **FastAPI**. It demonstrates the implementation of CRUD (Create, Read, Delete) operations with PostgreSQL as the database and Docker for containerization.

The application follows a layered architecture using repositories and services to keep the code modular and maintainable.

---

## Features

- Create a new student
- Get all students
- Get a student by ID
- Delete a student
- PostgreSQL database integration
- Docker and Docker Compose support
- Repository Pattern implementation
- Environment variable configuration

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL 16
- Psycopg2
- Pydantic
- Uvicorn
- Docker
- Docker Compose

---

## Project Structure

```
docker containerized backend/
│
├── app/
│   ├── models/
│   │   └── student.py
│   │
│   ├── repositories/
│   │   ├── repository.py
│   │   ├── postgres_repository.py
│   │   └── memory_repository.py
│   │
│   ├── routes/
│   │   └── students.py
│   │
│   ├── services/
│   │   └── student_service.py
│   │
│   ├── database.py
│   └── main.py
│
├── database/
│   └── init.sql
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Database Schema

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);
```

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd "docker containerized backend"
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/studentdb
```

---

## Running with Docker

Build and start the application:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d --build
```

Stop containers:

```bash
docker compose down
```

---

## Running without Docker

Start PostgreSQL locally.

Run the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

After running the server, open:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will be available.

---

## API Endpoints

### Create Student

**POST**

```
/students/
```

Example Request

```json
{
  "id": 1,
  "name": "Muhammad Ahmad",
  "email": "ahmad@example.com"
}
```

---

### Get All Students

**GET**

```
/students/
```

---

### Get Student by ID

**GET**

```
/students/{id}
```

Example

```
/students/1
```

---

### Delete Student

**DELETE**

```
/students/{id}
```

Example

```
/students/1
```

---

## Testing

The API can be tested using:

- Swagger UI
- Postman
- curl

Example:

```bash
curl http://127.0.0.1:8000/students/
```

---

## Docker Containers

The project runs two containers:

- **FastAPI Application**
- **PostgreSQL Database**

Docker Compose automatically starts both services.

---

## Design Pattern

This project follows the **Repository Pattern**.

Layers:

```
Client
   │
Routes
   │
Service
   │
Repository
   │
PostgreSQL
```

This separation improves:

- Maintainability
- Scalability
- Testability
- Code organization

---

## Environment Variables

| Variable | Description |
|-----------|-------------|
| DATABASE_URL | PostgreSQL connection string |

---

## Dependencies

Main packages used:

- fastapi
- uvicorn
- psycopg2-binary
- pydantic
- email-validator
- python-dotenv

---

## Future Improvements

- Update student endpoint
- Pagination
- Search functionality
- Unit testing
- JWT Authentication
- Async database operations
- Alembic database migrations
- CI/CD pipeline

---

## Author

**Muhammad Ahmad**

Backend Engineering Assignment – FlyRank

Built using FastAPI, PostgreSQL, and Docker.
