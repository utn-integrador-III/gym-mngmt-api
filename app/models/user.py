# app/models/user.py
from pydantic import BaseModel, Field
from typing import Optional
from app.models.shared import PyObjectId
from bson import ObjectId

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    username: str
    gender: Optional[str] = None
    phone: Optional[str] = None
    photo: Optional[str] = None

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "username": "user123",
                "gender": "male",
                "phone": "123456789",
                "photo": "http://example.com/photo.jpg"
            }
        }
