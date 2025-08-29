# app/models/user.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from app.models.shared import PyObjectId
from bson import ObjectId

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    password: str
    role: Literal["cliente", "entrenador", "admin"]
    gender: Literal["male", "female"]
    phone: Optional[str] = None
    photo: Optional[str] = None  # GridFS ObjectId en string

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "username": "user123",
                "email": "user@example.com",
                "password": "strongpassword123",
                "role": "cliente",
                "gender": "male",
                "phone": "123456789",
                "photo": "(archivo en form-data, no en JSON)"
            }
        }
