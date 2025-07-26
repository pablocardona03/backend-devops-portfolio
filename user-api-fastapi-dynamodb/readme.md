
# 🧩 User API - FastAPI + DynamoDB

Una API REST simple para gestionar usuarios utilizando **FastAPI** y **DynamoDB** como base de datos NoSQL.

## 🚀 Tecnologías

- **FastAPI** para el framework web
- **DynamoDB** (AWS) como base de datos NoSQL
- **Pydantic v2** para validación de datos
- **Uvicorn** como servidor ASGI
- **Boto3** para conectar con AWS DynamoDB
- **UUID4** para generación automática de ID únicos
- **dotenv** para variables de entorno

## 🗂️ Estructura del proyecto

```
user-api-fastapi-dynamodb/
├── app/
│   ├── main.py         # Punto de entrada de la app
│   ├── routes.py       # Rutas de usuario (CRUD)
│   ├── models.py       # Esquema de datos con Pydantic
│   └── dynamo.py       # Conexión con DynamoDB
├── .env                # Variables de entorno (no subir a git)
├── create_table.py     # Script opcional para crear tabla en DynamoDB
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

## ⚙️ Instalación

```bash
git clone https://github.com/tu-usuario/user-api-fastapi-dynamodb.git
cd user-api-fastapi-dynamodb

python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

pip install -r requirements.txt
```

## 🔐 Configura tus variables de entorno

Crea un archivo `.env` con tu configuración de AWS:

```
AWS_ACCESS_KEY_ID=TU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=TU_SECRET_KEY
AWS_REGION=us-east-1
```

## ▶️ Ejecución

```bash
uvicorn app.main:app --reload
```

Abre Swagger en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔁 Endpoints disponibles

| Método | Ruta             | Descripción                  |
|--------|------------------|------------------------------|
| POST   | /users           | Crear un nuevo usuario       |
| GET    | /users/{id}      | Obtener usuario por ID       |
| GET    | /users           | Listar todos los usuarios    |
| PUT    | /users/{id}      | Actualizar usuario existente |
| DELETE | /users/{id}      | Eliminar usuario por ID      |

## 🧪 Ejemplo CURL para crear un usuario

```bash
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d "{\"name\": \"Juan Pérez\", \"email\": \"juan@example.com\"}"
```

## ⚠️ Notas

- Ejecuta `create_table.py` solo si necesitas crear la tabla desde código.
- La validación de email se realiza usando `pydantic[email]`.

## 🧑 Autor

**Pablo César Cardona Rodríguez**  
Desarrollador Backend & DevOps Enthusiast

---

Proyecto desarrollado como parte de portafolio profesional.
