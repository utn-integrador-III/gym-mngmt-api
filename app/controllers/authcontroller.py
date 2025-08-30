# app/controllers/authcontroller.py
from fastapi import HTTPException
from typing import Optional, Any
from app.config.mongo import database

# Colección de usuarios
collection = database["users"]

# Intento de verificación con bcrypt si está disponible; si no, compara como texto plano (dev).
def _verify_password(plain: str, stored: str) -> bool:
    try:
        from passlib.context import CryptContext
        ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return ctx.verify(plain, stored)
    except Exception:
        # fallback: compara plano (no usar en producción)
        return plain == stored

def _to_str_id(v: Any) -> str:
    try:
        # ObjectId o cualquier cosa -> str
        return str(v)
    except Exception:
        return ""

async def login(email: str, password: str) -> dict:
    # Busca por email 
    user: Optional[dict] = await collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    stored = user.get("password") or ""
    if not _verify_password(password, stored):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # id y rol
    uid = _to_str_id(user.get("_id") or user.get("id"))
    role = user.get("role") or "user"

    return {"id": uid, "role": role, "message": "ok"}
