from fastapi import FastAPI
from app.routes.index import api_router as main_router

app = FastAPI()

# Montar todos los routers
app.include_router(main_router)
