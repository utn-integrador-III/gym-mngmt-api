# app/routes/assigned_routines.py
from fastapi import APIRouter
from app.models.assignedroutines import AssignedRoutinesModel
from app.controllers import assignedroutinescontroller as controller

router = APIRouter(prefix="/assignedroutines", tags=["Assigned Routines"])

@router.post("/", response_model=AssignedRoutinesModel)
async def create(data: AssignedRoutinesModel):
    return await controller.create_assigned_routine(data)

@router.get("/", response_model=list[AssignedRoutinesModel])
async def get_all():
    return await controller.get_all_assigned_routines()

@router.get("/{routine_id}", response_model=AssignedRoutinesModel)
async def get_one(routine_id: str):
    return await controller.get_assigned_routine(routine_id)

@router.put("/{routine_id}", response_model=AssignedRoutinesModel)
async def update(routine_id: str, data: AssignedRoutinesModel):
    return await controller.update_assigned_routine(routine_id, data)

@router.delete("/{routine_id}")
async def delete(routine_id: str):
    return await controller.delete_assigned_routine(routine_id)
