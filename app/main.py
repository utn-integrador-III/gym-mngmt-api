from fastapi import FastAPI
from app.routes.index import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Montar todos los routers
app.include_router(router)
