from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://utnuser:utnus3r24@cluster0.d9lhmxd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

DATABASE_NAME = "gym_management_db"  # gym_management_db

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
