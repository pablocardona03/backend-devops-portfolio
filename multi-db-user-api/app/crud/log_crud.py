from app.db.mongo import logs_collection
from app.schemas.log_schema import LogSchema
from datetime import datetime


async def create_log(action: str, user_id: str, details: dict):
    log = {
        "action": action,
        "user_id": user_id,
        "timestamp": datetime.utcnow(),
        "details": details
    }
    await logs_collection.insert_one(log)

async def get_logs():
    logs = []
    async for log in logs_collection.find():
        log["_id"] = str(log["_id"])
        logs.append(log)
    return logs
