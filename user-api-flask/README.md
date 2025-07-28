# User API - Basic RESTful Flask Application

This project is a simple REST API built with **Flask** that demonstrates the fundamental structure of a backend application using Python. It is intended as a starter project and does not use Docker or an external database.

---

## 📦 Tech Stack

- Python 3.10
- Flask 3.x
- (Optional) SQLite for local persistence

---

## 📁 Project Structure

```bash
user-api-flask/
├── app/
│   ├── __init__.py
│   └── routes.py
├── run.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project Locally

> Make sure Python 3.10+ is installed

1. Clone this repository
2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
```

3. Start the server:

```bash
python run.py
```

4. The API will be available at [http://localhost:5000](http://localhost:5000)

---

## ⚙️ Environment Variables

These variables are loaded from `.env` and used in the Flask app:

```env
MYSQL_HOST =localhost
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=userdb
```

---

## ✅ Steps to create the database and table:

1. Access MySQL from the terminal:

```bash
mysql -u root -p
```

2. Create the database and select it:

```bash
CREATE DATABASE userdb;
USE userdb;
```

3. Create the users table and insert example data:

```bash
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
  ('Juan', 'juan@example.com'),
  ('Maria', 'maria@example.com');
```

4. Ensure your Flask application is configured to connect to this database by setting the correct values for host, user, password, and database in `app/__init__.py`.

---

## 📚 API Endpoints

### 📤 `GET /users`
Returns a list of users (hardcoded or from SQLite)

### 📥 `POST /users`
Creates a new user

### ✏️ `PUT /users/<id>`
Updates an existing user

### ❌ `DELETE /users/<id>`
Deletes a user

---

## 🧠 Educational Value

This project is ideal for:

- Practicing Flask structure
- Learning REST API principles
- Building a foundation before adding Docker, CI/CD, etc.

---

## 📦 CURL Examples

### 📥 Create a user

```bash
curl -X POST http://localhost:5000/users   -H "Content-Type: application/json"   -d '{"name": "Pablo", "email": "pablo@example.com"}'
```

### 📤 Get all users

```bash
curl http://localhost:5000/users
```

### ✏️ Update a user

```bash
curl -X PUT http://localhost:5000/users/1   -H "Content-Type: application/json"   -d '{"name": "Updated Juan", "email": "juan@updated.com"}'
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

MIT License
