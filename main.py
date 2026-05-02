from fastapi import FastAPI
from src.utils.db import get_db, Base, engine
from src.tasks.models import TaskModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")


