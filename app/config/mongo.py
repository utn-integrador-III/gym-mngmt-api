from motor.motor_asyncio import AsyncIOMotorClient
import os

# Puedes usar variables de entorno para manejar la URI (más seguro)
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://utnuser:utnus3r24@cluster0.d9lhmxd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# Define aquí el nombre de la base de datos (puedes crearla desde MongoDB Atlas o la primera vez que insertes)
DATABASE_NAME = "gym_management_db"  # ejemplo: gym_management_db

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
