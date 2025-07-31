from fastapi import APIRouter
from app.db.mongo import logs_collection
from app.schemas.log_schema import LogSchema
from typing import List

@router.get("/", response_model=List[LogSchema])
async def get_logs():
    logs_cursor = logs_collection.find({})
    logs = await logs_cursor.to_list(length=100)  # Limita para no cargar demasiado
    return logs
