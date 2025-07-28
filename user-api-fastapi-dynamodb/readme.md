# 🧩 User API - FastAPI + DynamoDB

A simple REST API to manage users using **FastAPI** and **DynamoDB** as a NoSQL database.

## 🚀 Technologies

- **FastAPI** for the web framework  
- **DynamoDB** (AWS) as NoSQL database  
- **Pydantic v2** for data validation  
- **Uvicorn** as ASGI server  
- **Boto3** to connect with AWS DynamoDB  
- **UUID4** for automatic unique ID generation  
- **dotenv** for environment variables

## 🗂️ Project Structure

```
user-api-fastapi-dynamodb/
├── app/
│   ├── main.py         # App entry point
│   ├── routes.py       # User routes (CRUD)
│   ├── models.py       # Data schema with Pydantic
│   └── dynamo.py       # DynamoDB connection
├── .env                # Environment variables (don't upload to git)
├── create_table.py     # Optional script to create table in DynamoDB
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## ⚙️ Installation

```bash
git clone https://github.com/your-user/user-api-fastapi-dynamodb.git
cd user-api-fastapi-dynamodb

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

## 🔐 Set your environment variables

Create a `.env` file with your AWS config:

```
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
AWS_REGION=us-east-1
```

## ▶️ Run

```bash
uvicorn app.main:app --reload
```

Open Swagger at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔁 Available Endpoints

| Method | Path            | Description                   |
|--------|------------------|-------------------------------|
| POST   | /users           | Create a new user             |
| GET    | /users/{id}      | Get user by ID                |
| GET    | /users           | List all users                |
| PUT    | /users/{id}      | Update existing user          |
| DELETE | /users/{id}      | Delete user by ID             |

## 🧪 CURL Example to Create a User

```bash
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d "{\"name\": \"Juan Pérez\", \"email\": \"juan@example.com\"}"
```

## ⚠️ Notes

- Run `create_table.py` only if you need to create the table from code.
- Email validation is performed using `pydantic[email]`.

## 🧑 Author

**Pablo César Cardona Rodríguez**  
Backend Developer & DevOps Enthusiast

---

Project developed as part of professional portfolio.
