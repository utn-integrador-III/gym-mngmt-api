# app/routes/authroute.py
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.controllers import authcontroller

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginIn(BaseModel):
    email: EmailStr
    password: str

class LoginOut(BaseModel):
    id: str
    role: str
    message: str = "ok"

@router.post("/login", response_model=LoginOut)
async def login(payload: LoginIn):
    data = await authcontroller.login(payload.email, payload.password)
    return LoginOut(**data)
