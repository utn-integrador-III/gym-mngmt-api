from fastapi import APIRouter
from app.routes.userroute import router as user_router

router = APIRouter()

# Aquí incluyes tus routers individuales
router.include_router(user_router, prefix="/users", tags=["Users"])
