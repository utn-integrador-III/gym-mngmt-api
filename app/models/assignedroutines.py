# app/models/assigned_routines.py
from pydantic import BaseModel, Field
from typing import Optional, Literal
from app.models.shared import PyObjectId
from bson import ObjectId

class AssignedRoutinesModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    id_coach: PyObjectId = Field(...)
    id_client: PyObjectId = Field(...)
    id_dailyroutineexercise: PyObjectId = Field(...)
    notes: Optional[str] = None
    done: bool = False
    dayofweek: Literal[
        "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"
    ]

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id_coach": "60f7f9e0c8c8a2f1d8d0b9f5",
                "id_client": "60f7f9e0c8c8a2f1d8d0b9f6",
                "id_dailyroutineexercise": "60f7f9e0c8c8a2f1d8d0b9f7",
                "notes": "Focus on form and breathing",
                "done": False,
                "dayofweek": "lunes"
            }
        }
