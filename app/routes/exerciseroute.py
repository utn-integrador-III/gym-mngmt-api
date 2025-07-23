from fastapi import APIRouter
from app.controllers.exercisecontroller import (
    create_exercise, get_exercises, get_exercise,
    update_exercise, delete_exercise
)
from app.models.exercise import ExerciseModel

router = APIRouter(prefix="/exercises", tags=["Exercises"])

@router.post("/", response_model=ExerciseModel)
async def create(exercise: ExerciseModel):
    return await create_exercise(exercise)

@router.get("/", response_model=list[ExerciseModel])
async def read_all():
    return await get_exercises()

@router.get("/{exercise_id}", response_model=ExerciseModel)
async def read_one(exercise_id: str):
    return await get_exercise(exercise_id)

@router.put("/{exercise_id}", response_model=ExerciseModel)
async def update(exercise_id: str, exercise: ExerciseModel):
    return await update_exercise(exercise_id, exercise)

@router.delete("/{exercise_id}")
async def delete(exercise_id: str):
    return await delete_exercise(exercise_id)
