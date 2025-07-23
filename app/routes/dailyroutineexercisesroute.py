from fastapi import APIRouter
from app.models.dailyroutineexercises import DailyRoutineExercisesModel
from app.controllers import dailyroutineexercisescontroller

router = APIRouter()

@router.post("/", response_model=DailyRoutineExercisesModel)
async def create_routine(routine: DailyRoutineExercisesModel):
    return await dailyroutineexercisescontroller.create_routine(routine)

@router.get("/", response_model=list[DailyRoutineExercisesModel])
async def get_all_routines():
    return await dailyroutineexercisescontroller.get_all_routines()

@router.get("/{routine_id}", response_model=DailyRoutineExercisesModel)
async def get_routine(routine_id: str):
    return await dailyroutineexercisescontroller.get_routine(routine_id)

@router.put("/{routine_id}", response_model=DailyRoutineExercisesModel)
async def update_routine(routine_id: str, updated_routine: DailyRoutineExercisesModel):
    return await dailyroutineexercisescontroller.update_routine(routine_id, updated_routine)

@router.delete("/{routine_id}")
async def delete_routine(routine_id: str):
    return await dailyroutineexercisescontroller.delete_routine(routine_id)
