from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from src.utils.Messages import messages
from src.utils.response import api_response
from src.utils.constant import status_code

def create_task(body: TaskSchema, db: Session):
    """Create a new task and save it to the database."""
    new_task = TaskModel(
        title=body.title,
        description=body.description,
        due_date=body.due_date,
        completed=body.is_completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return api_response(data=new_task.to_dict(), message=messages.TASK_CREATED, status_code=status_code.CREATED)


def get_tasks(db: Session):
    """Retrieve all tasks from the database."""
    tasks = db.query(TaskModel).all()
    return api_response(message=messages.TASKS_RETRIEVED, data=[task.to_dict() for task in tasks], status_code=status_code.OK)


def get_task(task_id: int, db: Session):
    """Retrieve a single task by its ID. Returns 404 if not found."""
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        api_response(success=False, message=messages.TASK_NOT_FOUND, status_code=status_code.NOT_FOUND)
    return api_response(message=messages.TASK_RETRIEVED, data=task.to_dict(), status_code=status_code.OK)

def update_task(task_id: int, body: TaskSchema, db: Session):
    """Update an existing task by its ID. Returns 404 if not found."""
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        api_response(success=False, message=messages.TASK_NOT_FOUND, status_code=status_code.NOT_FOUND)

    task.title = body.title
    task.description = body.description
    task.due_date = body.due_date
    task.completed = body.is_completed

    db.commit()
    db.refresh(task)
    return api_response(data=task.to_dict(), message=messages.TASK_UPDATED, status_code=status_code.OK)

def delete_task(task_id: int, db: Session):
    """Delete a task by its ID. Returns 404 if not found."""
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        api_response(success=False, message=messages.TASK_NOT_FOUND, status_code=status_code.NOT_FOUND)

    db.delete(task)
    db.commit()
    return api_response(message=messages.TASK_DELETED, status_code=status_code.OK)
