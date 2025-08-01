from fastapi import APIRouter
from app.routes import userroute, exerciseroute, dailyroutineexercisesroute, assignedroutinesroute

router = APIRouter()

# Include the user routes
router.include_router(userroute.router)

# Include the exercise routes
router.include_router(exerciseroute.router)

# Include the daily routine exercises routes, another way to structure the prefix and tags
router.include_router(dailyroutineexercisesroute.router, prefix="/dailyroutines", tags=["Daily Routines"])

# Include the assigned routines routes
router.include_router(assignedroutinesroute.router)