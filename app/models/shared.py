# app/models/shared.py

from bson import ObjectId
from typing import Any
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue

class PyObjectId(ObjectId):

    @classmethod
    def __get_pydantic_core_schema__(cls, _source_type: Any, _handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            python_schema=core_schema.no_info_plain_validator_function(cls.validate),
            json_schema=core_schema.no_info_plain_validator_function(cls.validate),
            serialization=core_schema.plain_serializer_function_ser_schema(lambda v: str(v))
        )

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if isinstance(v, ObjectId):
            return v
        if isinstance(v, str):
            return ObjectId(v)
        raise TypeError("Invalid ObjectId")

    def __repr__(self) -> str:
        return f"ObjectId('{str(self)}')"
    
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return {
            "type": "string",
            "format": "objectid",
            "examples": ["507f1f77bcf86cd799439011"],
        }
# app/models/shared.py