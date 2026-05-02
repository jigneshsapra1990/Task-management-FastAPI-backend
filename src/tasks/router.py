from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from src.utils.constant import routes
from sqlalchemy.orm import Session

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

# Create a new task
@tasks_router.post(routes.CREATE, response_model=dict)
def create_task(body: TaskSchema, db: Session = Depends(get_db)):
    return controller.create_task(body, db)


# Get all tasks
@tasks_router.get(routes.GET_ALL)
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)

# Get a single task by ID
@tasks_router.get(routes.GET_BY_ID)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return controller.get_task(task_id, db)

# Update a task by ID
@tasks_router.put(routes.UPDATE)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db)):
    return controller.update_task(task_id, body, db)

# Delete a task by ID
@tasks_router.delete(routes.DELETE)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return controller.delete_task(task_id, db)

