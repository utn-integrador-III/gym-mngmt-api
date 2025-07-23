from fastapi import HTTPException
from bson import ObjectId
from app.models.dailyroutineexercises import DailyRoutineExercisesModel
from app.config.mongo import database

collection = database["daily_routines"]

async def create_routine(routine: DailyRoutineExercisesModel):
    result = await collection.insert_one(routine.dict(by_alias=True))
    routine.id = result.inserted_id
    return routine

async def get_all_routines():
    routines = await collection.find().to_list(1000)
    return routines

async def get_routine(routine_id: str):
    routine = await collection.find_one({"_id": ObjectId(routine_id)})
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    return routine

async def update_routine(routine_id: str, updated_routine: DailyRoutineExercisesModel):
    updated = await collection.find_one_and_update(
        {"_id": ObjectId(routine_id)},
        {"$set": updated_routine.dict(by_alias=True, exclude={"id"})},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    return updated

async def delete_routine(routine_id: str):
    result = await collection.delete_one({"_id": ObjectId(routine_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    return {"message": "Rutina eliminada"}
