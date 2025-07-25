# User Management App with Flask, MySQL, and Docker

This project is a full-stack user management application built with **Flask**, **MySQL**, and **Docker**, featuring a clean frontend UI integrated with backend CRUD functionality. It demonstrates professional software development practices and is ready for deployment or further extension.

---

## 🚀 Features

- Full CRUD operations with web interface (create, read, update, delete users)
- Input validation with email format check
- Modular Flask architecture using Blueprints
- Dockerized setup with Docker Compose
- Auto-initialization of MySQL database with sample data
- Responsive frontend using HTML, CSS and Jinja2 templates

---

## 🛠 Tech Stack

- Python 3.10
- Flask 3.1.1
- MySQL 8.0
- HTML5, CSS3, Jinja2
- Docker & Docker Compose

---

## 📁 Project Structure

```bash
user-management-app/
├── app/
│   ├── __init__.py            # App factory and MySQL config
│   ├── routes.py              # Main routes and logic
│   └── templates/             # Frontend HTML templates
│       ├── index.html
│       ├── users.html
│       └── edit_user.html
├── db-init/
│   └── init.sql               # SQL script for DB bootstrap
├── run.py                     # App entry point
├── Dockerfile                 # Flask app container
├── docker-compose.yml         # Services: Flask + MySQL
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables for DB
└── README.md
```

---

## ⚙️ Environment Variables

Defined in `.env` file and used by Flask and MySQL containers:

```env
MYSQL_HOST=db
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=userdb
```

---

## 🧪 How to Run the App

> Make sure Docker and Docker Compose are installed on your system

1. Clone the repository:

```bash
git clone https://github.com/yourusername/user-management-app.git
cd user-management-app
```

2. Build and run the services:

```bash
docker-compose up --build
```

3. Open your browser and go to: [http://localhost:5000](http://localhost:5000)

4. You can now create, view, edit, and delete users from the web interface.

---

## 🗃️ Sample Data

The database is auto-initialized with the following structure and users:

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

## 📌 Notes

- Email input is validated using regex on the backend.
- Proper error messages are shown if fields are missing or incorrect.
- Page redirection and form submission are handled seamlessly using Flask.

---

## 🪪 License

This project is open-source and licensed under the MIT License.
