# app/routes/userroute.py
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from app.controllers import usercontroller
from app.models.user import UserModel

router = APIRouter(prefix="/users", tags=["Users"])

# ----------------- Crear usuario con opción de foto -----------------
@router.post("/", response_model=UserModel)
async def create(
    username: str = Form(...),
    gender: str = Form(...),
    phone: str = Form(None),
    photo: UploadFile = File(None)
):
    user = UserModel(username=username, gender=gender, phone=phone)
    photo_bytes = await photo.read() if photo else None
    photo_filename = photo.filename if photo else None
    return await usercontroller.create_user(user, photo_bytes, photo_filename)

# ----------------- Listar usuarios -----------------
@router.get("/", response_model=list[UserModel])
async def list_users():
    return await usercontroller.get_users()

# ----------------- Obtener un usuario -----------------
@router.get("/{user_id}", response_model=UserModel)
async def get(user_id: str):
    return await usercontroller.get_user(user_id)

# ----------------- Actualizar usuario con opción de foto -----------------
@router.put("/{user_id}", response_model=UserModel)
async def update(
    user_id: str,
    username: str = Form(None),
    gender: str = Form(None),
    phone: str = Form(None),
    photo: UploadFile = File(None)
):
    # Crear diccionario solo con los campos enviados
    user_dict = {k: v for k, v in {
        "username": username,
        "gender": gender,
        "phone": phone
    }.items() if v is not None}

    if not user_dict and not photo:
        raise HTTPException(status_code=400, detail="No data provided to update")

    user = UserModel(**user_dict)
    photo_bytes = await photo.read() if photo else None
    photo_filename = photo.filename if photo else None
    return await usercontroller.update_user(user_id, user, photo_bytes, photo_filename)

# ----------------- Eliminar usuario -----------------
@router.delete("/{user_id}")
async def delete(user_id: str):
    return await usercontroller.delete_user(user_id)

# ----------------- Descargar foto del usuario -----------------
@router.get("/{user_id}/photo")
async def download_photo(user_id: str):
    file_bytes = await usercontroller.download_user_photo(user_id)
    # Se envía el archivo como streaming
    return StreamingResponse(BytesIO(file_bytes), media_type="image/jpeg")
