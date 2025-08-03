
# Multi-Database User API (FastAPI + PostgreSQL + MongoDB)

This project is a fully containerized RESTful API for user management, built with **FastAPI**, **PostgreSQL**, and **MongoDB**, using **Docker** for environment orchestration. It includes secure authentication with **JWT**, hashed passwords, and role-based route protection. All logs of CRUD operations are stored in MongoDB.

---

## 📦 Features

- 🔐 User authentication and authorization with JWT tokens
- 🐘 Relational data in PostgreSQL (users)
- 🍃 Log storage in MongoDB (create/update/delete actions)
- 🧂 Password hashing with bcrypt
- ✅ Input validation with Pydantic
- 🐳 Dockerized architecture
- 🧪 Swagger documentation available at `/docs`
- 🧠 Clean modular architecture

---

## 🛠️ Tech Stack

- **FastAPI** – web framework
- **PostgreSQL** – main database for users
- **MongoDB** – secondary NoSQL database for logs
- **SQLAlchemy** + **AsyncSession** – database interaction
- **Pydantic v2** – schema validation
- **Docker & Docker Compose** – environment setup
- **bcrypt** – password hashing
- **python-jose** – JWT management

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/pablocardona03/backend-devops-portfolio.git
cd backend-devops-portfolio/multi-db-user-api
```

### 2. Environment setup

Create a `.env` file like this:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=users_db
POSTGRES_PORT=5432

MONGO_URI=mongodb://admin:admin@mongo:27017/
MONGO_DB=logs_db

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Build and run with Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

---

## 🔐 Authentication

### 1. Register a new user

`POST /auth/register`  
Body:

```json
{
  "username": "admin",
  "password": "securepassword"
}
```

### 2. Authorize in Swagger

Click the "Authorize" button in `/docs` and use your credentials:

---

## 📡 Protected Routes

All routes under `/users` are protected and require JWT authentication.

- `GET /users/` – List all users
- `GET /users/{id}` – Retrieve a user by ID
- `POST /users/` – Create a new user
- `PUT /users/{id}` – Update user
- `DELETE /users/{id}` – Delete user

All create/update/delete actions are logged in MongoDB automatically.

---

## 🧠 Project Structure

```
multi-db-user-api/
├── app/
│   ├── config/          # Environment and settings
│   ├── crud/            # Database logic
│   ├── db/              # DB connections
│   ├── models/          # ORM models
│   ├── routes/          # API endpoints
│   ├── schemas/         # Pydantic schemas
│   ├── services/        # Auth and utilities
│   └── main.py          # App entrypoint
├── docker-compose.yml
├── Dockerfile
└── README.md
```
