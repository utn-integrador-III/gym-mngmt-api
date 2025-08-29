# app/models/daily_routine_exercise.py

from pydantic import BaseModel, Field
from typing import Optional, List
from app.models.shared import PyObjectId

class DailyRoutineExercisesModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    id_coach: PyObjectId = Field(...)
    id_exercise: List[PyObjectId] = Field(...)
    name: str

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id_coach": "60f7f9e0c8c8a2f1d8d0b9f5",
                "id_exercise": [
                    "60f7f9e0c8c8a2f1d8d0b9f6",
                    "60f7f9e0c8c8a2f1d8d0b9f7"
                ],
                "name": "Morning Upper Body Routine"
            }
        }
# app/models/daily_routine_exercise.py