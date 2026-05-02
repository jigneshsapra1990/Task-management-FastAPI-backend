from fastapi import FastAPI
from src.utils.db import engine
from src.tasks.models import Base, TaskModel
from src.tasks.router import tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.include_router(tasks_router)

