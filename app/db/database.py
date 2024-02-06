from motor.motor_asyncio import AsyncIOMotorClient
import os

class DataBase:
    client: AsyncIOMotorClient = None
    db = None

db = DataBase()

def get_database_url() -> str:
    # Fetch the database URL from environment variables or configuration
    return os.getenv("DEV_DB_URL")

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(get_database_url())
    # db.db = db.client.get_default_database()
    db.db = db.client["fastapi-db"]   # Adjust 'mydatabase' as needed

async def close_mongo_connection():
    db.client.close()

def get_db():
    return db.db
