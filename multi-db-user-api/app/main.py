from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user_routes, log_routes
from app.db.postgres import Base, engine
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_postgres():
    print("🔄 Waiting for PostgreSQL to be ready...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname="users_db",
                user="user",
                password="password",
                host="postgres", 
                port="5432"
            )
            conn.close()
            print("✅ PostgreSQL is ready!")
            break
        except OperationalError:
            print("⏳ PostgreSQL not ready yet, retrying in 1 second...")
            time.sleep(1)

wait_for_postgres()

app = FastAPI(
    title="Multi-DB User API",
    description="API that uses PostgreSQL for user data and MongoDB for logging",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(log_routes.router, prefix="/logs", tags=["Logs"])


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Multi-DB User API"}
