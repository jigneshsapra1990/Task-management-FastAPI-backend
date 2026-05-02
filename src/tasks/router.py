from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

@tasks_router.post("/create", response_model=dict)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


@tasks_router.get("/all")
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)

@tasks_router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_task(task_id, db)

