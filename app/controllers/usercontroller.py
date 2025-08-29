# app/controllers/usercontroller.py
from fastapi import HTTPException
from bson import ObjectId
from app.models.user import UserModel
from app.config.mongo import database
from app.services.gridfs_service import GridFSService

collection = database["users"]
gridfs = GridFSService(database)

# ----------------- CRUD -----------------

async def create_user(user: UserModel, photo_bytes: bytes = None, photo_filename: str = None):
    """
    Crea un usuario. 
    Si se envía photo_bytes, se sube a GridFS y se guarda su ObjectId en 'photo'.
    """
    user_dict = user.dict(by_alias=True, exclude={"id"})

    # Subir foto si existe
    if photo_bytes and photo_filename:
        photo_id = await gridfs.upload_file(photo_bytes, photo_filename)
        user_dict["photo"] = str(photo_id)

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

async def update_user(user_id: str, user: UserModel, photo_bytes: bytes = None, photo_filename: str = None):
    """
    Actualiza un usuario. 
    Puede reemplazar la foto si se envían photo_bytes y photo_filename.
    """
    user_dict = user.dict(by_alias=True, exclude_unset=True, exclude={"id"})

    # Subir nueva foto si se proporciona
    if photo_bytes and photo_filename:
        # Opcional: eliminar foto anterior
        existing_user = await collection.find_one({"_id": ObjectId(user_id)})
        if existing_user and existing_user.get("photo"):
            await gridfs.delete_file(existing_user["photo"])

        photo_id = await gridfs.upload_file(photo_bytes, photo_filename)
        user_dict["photo"] = str(photo_id)

    result = await collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict})
    if result.modified_count == 1:
        updated_user = await collection.find_one({"_id": ObjectId(user_id)})
        if updated_user:
            updated_user["_id"] = str(updated_user["_id"])
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

async def delete_user(user_id: str):
    # Eliminar foto si existe
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if user and user.get("photo"):
        await gridfs.delete_file(user["photo"])

    result = await collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# ----------------- Opcional: descargar foto -----------------
async def download_user_photo(user_id: str) -> bytes:
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if not user or not user.get("photo"):
        raise HTTPException(status_code=404, detail="Photo not found")
    file_bytes = await gridfs.download_file(user["photo"])
    if not file_bytes:
        raise HTTPException(status_code=404, detail="Photo not found in GridFS")
    return file_bytes
