from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class LogSchema(BaseModel):
    action: str
    user_id: str
    timestamp: datetime
    details: Dict

    class Config:
        orm_mode = True
