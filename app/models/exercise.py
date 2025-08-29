from pydantic import BaseModel, Field
from typing import Optional
from app.models.shared import PyObjectId
from bson import ObjectId

class ExerciseModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "name": "Push Ups",
                "description": "Upper body exercise using body weight"
            }
        }
