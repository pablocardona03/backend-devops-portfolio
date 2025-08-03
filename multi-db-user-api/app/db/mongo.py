from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection

MONGO_URL = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URL)

db = client["log_db"]
logs_collection: Collection = db["logs"]