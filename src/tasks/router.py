from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

@tasks_router.post("/create", response_model=dict)
def create_task_route(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)
