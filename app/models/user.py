from pydantic import BaseModel, Field
from typing import Literal, Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return v
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        schema = handler(core_schema)
        schema.update(type="string")
        return schema


class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    username: str
    #role: Literal["coach", "client"]
    #password: str
    gender: Optional[str] = None
    phone: Optional[str] = None
    photo: Optional[str] = None

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "username": "user123",
                #"role": "client",
                #"password": "securepassword",
                "gender": "male",
                "phone": "123456789",
                "photo": "http://example.com/photo.jpg"
            }
        }
