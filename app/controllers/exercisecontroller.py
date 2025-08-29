from fastapi import HTTPException
from bson import ObjectId
from app.models.exercise import ExerciseModel
from app.config.mongo import database

collection = database["exercises"]

async def create_exercise(exercise: ExerciseModel):
    exercise_dict = exercise.dict(by_alias=True, exclude={"id"})
    result = await collection.insert_one(exercise_dict)
    exercise_dict["_id"] = str(result.inserted_id)
    return exercise_dict

async def get_exercises():
    exercises = await collection.find().to_list(1000)
    for exercise in exercises:
        exercise["_id"] = str(exercise["_id"])
    return exercises

async def get_exercise(exercise_id: str):
    exercise = await collection.find_one({"_id": ObjectId(exercise_id)})
    if exercise:
        exercise["_id"] = str(exercise["_id"])
        return exercise
    raise HTTPException(status_code=404, detail="Exercise not found")

async def update_exercise(exercise_id: str, exercise: ExerciseModel):
    exercise_dict = exercise.dict(by_alias=True, exclude_unset=True, exclude={"id"})
    result = await collection.update_one(
        {"_id": ObjectId(exercise_id)},
        {"$set": exercise_dict}
    )
    if result.modified_count == 1:
        updated = await collection.find_one({"_id": ObjectId(exercise_id)})
        if updated:
            updated["_id"] = str(updated["_id"])
            return updated
    raise HTTPException(status_code=404, detail="Exercise not found")

async def delete_exercise(exercise_id: str):
    result = await collection.delete_one({"_id": ObjectId(exercise_id)})
    if result.deleted_count == 1:
        return {"message": "Exercise deleted"}
    raise HTTPException(status_code=404, detail="Exercise not found")
