# User API with Flask, MySQL and Docker

This is a full CRUD REST API built with **Flask** and **MySQL**, containerized using **Docker** and **Docker Compose**. It demonstrates professional practices such as:

- Modular Flask application structure
- Input validation
- Docker-based multi-service architecture
- Database auto-initialization with sample data

---

## 📦 Tech Stack

- Python 3.10
- Flask 3.1.1
- MySQL 8.0
- Docker & Docker Compose
- SQL for DB bootstrap
- Manual testing with `curl` or Postman

---

## 📁 Project Structure

```bash
user-api-flask/
├── app/                        # Flask app code (routes, init)
│   ├── __init__.py
│   └── routes.py
├── db-init/                   # SQL script to initialize the DB
│   └── init.sql
├── run.py                     # Entry point for Flask app
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Flask container build
├── docker-compose.yml         # Compose configuration for Flask + MySQL
├── .env                       # Environment variables for DB connection
└── README.md
```

---

## ⚙️ Environment Variables

These variables are loaded from `.env` and used in the Flask app:

```env
MYSQL_HOST=db
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=userdb
```

---

## 🚀 How to Run the Project

> **Make sure Docker and Docker Compose are installed**

1. Clone this repo  
2. Build and start the services:

```bash
docker-compose up --build
```

3. Access the API at [http://localhost:5000](http://localhost:5000)

4. Database is auto-created with sample users

---

## 🗃️ Sample Data

The database initializes with this table and data:

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
  ('Juan', 'juan@example.com'),
  ('Maria', 'maria@example.com');
```

---

## 🧪 Testing the API

You can test all endpoints using `curl` from your terminal.

### 📥 Create a user

```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Pablo", "email": "pablo@example.com"}'
```

### 📤 Get all users

```bash
curl http://localhost:5000/users
```

### ✏️ Update a user

```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Juan", "email": "juan@updated.com"}'
```

### ❌ Delete a user

```bash
curl -X DELETE http://localhost:5000/users/1
```

---

## 📌 Notes

- The API validates email format using regex
- `404` is returned if you try to edit/delete a non-existing user
- The project uses Flask’s built-in server, suitable for development only


---

## 📄 License

This project is open-source and licensed under the MIT License.
