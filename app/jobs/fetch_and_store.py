import httpx
from app.db.database import db

async def fetch_and_store():
    async with httpx.AsyncClient() as client:
        # @ToDo: Use API URL env
        response = await client.get("https://api.external.com/data")
        data = response.json()
        # Process data if needed
        processed_data = {"processed": data}  # Example processed data
        # Store in MongoDB
        await db.db["collection_name"].insert_one(data)  # Adjust 'collection_name' as needed
