async def log_operation(action: str, user_id: str, details: dict):
    log = {
        "action": action,
        "user_id": user_id,
        "timestamp": datetime.utcnow(),
        "details": details
    }
    await logs_collection.insert_one(log)
