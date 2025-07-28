from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import user_routes, log_routes

app = FastAPI(
    title="Multi-DB User API",
    description="API that uses PostgreSQL for user data and MongoDB for logging",
    version="1.0.0"
)

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
