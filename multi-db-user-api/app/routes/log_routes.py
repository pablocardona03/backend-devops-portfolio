from fastapi import APIRouter
from typing import List
from app.schemas.log_schema import LogSchema
from app.db.mongo import logs_collection
from pydantic import BaseModel
from typing import Dict
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[LogSchema])
async def get_logs():
    logs_cursor = logs_collection.find({})
    logs = await logs_cursor.to_list(length=100)

    cleaned_logs = []
    for log in logs:
        log.pop("_id", None) 
        cleaned_logs.append(log)
    
    return cleaned_logs

class LogSchema(BaseModel):
    action: str
    user_id: str
    timestamp: datetime
    details: Dict

    class Config:
        from_attributes = True
