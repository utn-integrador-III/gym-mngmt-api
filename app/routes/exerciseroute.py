from fastapi import APIRouter, HTTPException
from bson import ObjectId
from app.models.exercise import ExerciseModel
from app.config.mongo import database

router = APIRouter()
collection = database["exercises"]

@router.post("/", response_model=ExerciseModel)
async def create_exercise(exercise: ExerciseModel):
    exercise_dict = exercise.dict(by_alias=True, exclude={"id"})  # Excluir "id"
    result = await collection.insert_one(exercise_dict)
    exercise_dict["_id"] = str(result.inserted_id)  # Convertir a str
    return exercise_dict

@router.get("/", response_model=list[ExerciseModel])
async def get_exercises():
    exercises = await collection.find().to_list(1000)
    for exercise in exercises:
        exercise["_id"] = str(exercise["_id"])  # Convertir ObjectId a str
    return exercises

@router.get("/{exercise_id}", response_model=ExerciseModel)
async def get_exercise(exercise_id: str):
    exercise = await collection.find_one({"_id": ObjectId(exercise_id)})
    if exercise:
        exercise["_id"] = str(exercise["_id"])
        return exercise
    raise HTTPException(status_code=404, detail="Exercise not found")

@router.put("/{exercise_id}", response_model=ExerciseModel)
async def update_exercise(exercise_id: str, exercise: ExerciseModel):
    exercise_dict = exercise.dict(by_alias=True, exclude_unset=True, exclude={"id"})
    result = await collection.update_one(
        {"_id": ObjectId(exercise_id)},
        {"$set": exercise_dict}
    )
    if result.modified_count == 1:
        updated_exercise = await collection.find_one({"_id": ObjectId(exercise_id)})
        if updated_exercise:
            updated_exercise["_id"] = str(updated_exercise["_id"])
            return updated_exercise
    raise HTTPException(status_code=404, detail="Exercise not found")

@router.delete("/{exercise_id}")
async def delete_exercise(exercise_id: str):
    result = await collection.delete_one({"_id": ObjectId(exercise_id)})
    if result.deleted_count == 1:
        return {"message": "Exercise deleted"}
    raise HTTPException(status_code=404, detail="Exercise not found")
