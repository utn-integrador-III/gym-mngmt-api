from motor.motor_asyncio import AsyncIOMotorClient
import os

# opcion: usar variables de entorno para manejar la URI (más seguro)
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://utnuser:utnus3r24@cluster0.d9lhmxd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

# aquí se pasa el nombre de la base de datos (se puede crear desde MongoDB Atlas o la primera vez que inserte)
DATABASE_NAME = "gym_management_db"  # gym_management_db

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]
