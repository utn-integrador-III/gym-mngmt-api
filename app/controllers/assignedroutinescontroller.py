# app/controllers/assigned_routines.py
from fastapi import HTTPException
from bson import ObjectId
from app.config.mongo import database
from app.models.assignedroutines import AssignedRoutinesModel

collection = database["assigned_routines"]

async def create_assigned_routine(data: AssignedRoutinesModel):
    result = await collection.insert_one(data.dict(by_alias=True, exclude={"id"}))
    data.id = result.inserted_id
    return data

async def get_all_assigned_routines():
    routines = await collection.find().to_list(1000)
    return routines

async def get_assigned_routine(routine_id: str):
    routine = await collection.find_one({"_id": ObjectId(routine_id)})
    if not routine:
        raise HTTPException(status_code=404, detail="Rutina asignada no encontrada")
    return routine

async def update_assigned_routine(routine_id: str, updated_data: AssignedRoutinesModel):
    updated = await collection.find_one_and_update(
        {"_id": ObjectId(routine_id)},
        {"$set": updated_data.dict(by_alias=True, exclude={"id"})},
        return_document=True
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Rutina asignada no encontrada")
    return updated

async def delete_assigned_routine(routine_id: str):
    result = await collection.delete_one({"_id": ObjectId(routine_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Rutina asignada no encontrada")
    return {"message": "Rutina asignada eliminada"}
