from fastapi import HTTPException
from bson import ObjectId
from app.models.user import UserModel
from app.config.mongo import database

collection = database["users"]

async def create_user(user: UserModel):
    user_dict = user.dict(by_alias=True, exclude={"id"})
    result = await collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

async def get_users():
    users = await collection.find().to_list(1000)
    for user in users:
        user["_id"] = str(user["_id"])
    return users

async def get_user(user_id: str):
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return user
    raise HTTPException(status_code=404, detail="User not found")

async def update_user(user_id: str, user: UserModel):
    user_dict = user.dict(by_alias=True, exclude_unset=True, exclude={"id"})
    result = await collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})
    if result.modified_count == 1:
        updated_user = await collection.find_one({"_id": ObjectId(user_id)})
        if updated_user:
            updated_user["_id"] = str(updated_user["_id"])
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

async def delete_user(user_id: str):
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
