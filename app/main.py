from fastapi import FastAPI
from app.routes.index import router

app = FastAPI()

# Montar todos los routers
app.include_router(router)
