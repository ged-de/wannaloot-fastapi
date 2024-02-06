from contextlib import asynccontextmanager
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.jobs.fetch_and_store import fetch_and_store 
from app.db.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Database connection
    await connect_to_mongo()
    print("Database connected")

    # Setup scheduler
    # scheduler = AsyncIOScheduler()
    # scheduler.add_job(fetch_and_store, IntervalTrigger(minutes=10))
    # scheduler.start()

    yield  # Application is now running, scheduler jobs are active
    
    # Shutdown logic
    # scheduler.shutdown()
    await close_mongo_connection()
    print("Database connection closed")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
