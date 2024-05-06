from fastapi import FastAPI
from routers import router as employee_router
from auth import router as auth_router
from models import Base
from db import engine

Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI()

app.include_router(employee_router)  
app.include_router(auth_router)
