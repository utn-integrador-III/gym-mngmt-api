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

async def update_routine(routine_id: str, payload: DailyRoutineExercisesModel):
    q = {"_id": ObjectId(routine_id)} if ObjectId.is_valid(routine_id) else {"_id": routine_id}
    # prepara $set con los campos que aceptas actualizar:
    update_doc = {
        "$set": {
            "name": payload.name,
            "id_coach": ObjectId(payload.id_coach) if ObjectId.is_valid(str(payload.id_coach)) else payload.id_coach,
            "id_exercise": [
                ObjectId(x) if ObjectId.is_valid(str(x)) else x for x in payload.id_exercise
            ]
        }
    }
    res = await collection.update_one(q, update_doc)
    if res.matched_count == 0:
        raise HTTPException(status_code=404, detail="Rutina no encontrada")
    return {"message": "Rutina actualizada"}

# Aporte de Su
async def delete_routine(routine_id: str):
    # 1) intenta por ObjectId
    if ObjectId.is_valid(routine_id):
        res = await collection.delete_one({"_id": ObjectId(routine_id)})
        if res.deleted_count > 0:
            return {"message": "Rutina eliminada"}

    # 2) Fallback:  _id string 
    res = await collection.delete_one({"_id": routine_id})
    if res.deleted_count > 0:
        return {"message": "Rutina eliminada"}

    # Nada coincidió
    raise HTTPException(status_code=404, detail="Rutina no encontrada")