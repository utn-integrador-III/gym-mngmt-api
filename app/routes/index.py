from fastapi import APIRouter
from app.routes import userroute, exerciseroute

api_router = APIRouter()

# Usuarios bajo /users
api_router.include_router(userroute.router, prefix="/users", tags=["Users"])

# Ejercicios bajo /exercises
api_router.include_router(exerciseroute.router, prefix="/exercises", tags=["Exercises"])
