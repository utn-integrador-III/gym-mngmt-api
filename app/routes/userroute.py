from fastapi import APIRouter
from app.controllers import usercontroller
from app.models.user import UserModel

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserModel)
async def create(user: UserModel):
    return await usercontroller.create_user(user)

@router.get("/", response_model=list[UserModel])
async def list_users():
    return await usercontroller.get_users()

@router.get("/{user_id}", response_model=UserModel)
async def get(user_id: str):
    return await usercontroller.get_user(user_id)

@router.put("/{user_id}", response_model=UserModel)
async def update(user_id: str, user: UserModel):
    return await usercontroller.update_user(user_id, user)

@router.delete("/{user_id}")
async def delete(user_id: str):
    return await usercontroller.delete_user(user_id)
