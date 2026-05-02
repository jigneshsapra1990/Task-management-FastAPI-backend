from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from src.utils.constant import routes, status_code
from sqlalchemy.orm import Session
from src.utils.helpers import is_authenticated
from src.user.models import UserModel

tasks_router = APIRouter(prefix="/tasks", tags=["tasks"])

# Create a new task
@tasks_router.post(routes.CREATE, status_code=status_code.CREATED )
def create_task(body: TaskSchema, db: Session = Depends(get_db), user:UserModel =Depends(is_authenticated)):
    return controller.create_task(body, db,user)

# Get all tasks
@tasks_router.get(routes.GET_ALL, status_code=status_code.OK)
def get_tasks(db: Session = Depends(get_db), user:UserModel =Depends(is_authenticated)):
    return controller.get_tasks(db)

# Get a single task by ID
@tasks_router.get(routes.GET_BY_ID, status_code=status_code.OK)
def get_task(task_id: int, db: Session = Depends(get_db), user:UserModel =Depends(is_authenticated)):
    return controller.get_task(task_id, db)

# Update a task by ID
@tasks_router.put(routes.UPDATE, status_code=status_code.OK)
def update_task(task_id: int, body: TaskSchema, db: Session = Depends(get_db), user:UserModel =Depends(is_authenticated)):
    return controller.update_task(task_id, body, db,user)

# Delete a task by ID
@tasks_router.delete(routes.DELETE, status_code=status_code.OK)
def delete_task(task_id: int, db: Session = Depends(get_db), user:UserModel =Depends(is_authenticated)):
    return controller.delete_task(task_id, db)
