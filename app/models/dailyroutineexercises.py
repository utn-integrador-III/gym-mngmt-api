from pydantic import BaseModel, Field
from typing import Optional
from app.models.shared import PyObjectId
from bson import ObjectId

class DailyRoutineExercisesModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    id_coach: PyObjectId = Field(...)
    id_exercise: PyObjectId = Field(...)
    name: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id_coach": "60f7f9e0c8c8a2f1d8d0b9f5",
                "id_exercise": "60f7f9e0c8c8a2f1d8d0b9f6",
                "name": "Morning Upper Body Routine"
            }
        }
