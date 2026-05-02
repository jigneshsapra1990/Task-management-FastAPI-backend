from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.utils.Messages import messages
from src.utils.response import success_response, error_response

def create_task(body: TaskSchema, db:Session):
    new_task = TaskModel(
        title=body.title,
        description=body.description,
        due_date=body.due_date,
        completed=body.is_completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return success_response(data=new_task, message=messages.TASK_CREATED, status_code=201)


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return success_response(data=tasks)


def get_task(task_id: int, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=error_response(message=messages.TASK_NOT_FOUND, status_code=404))
    return success_response(data=task)

def update_task(task_id: int, body: TaskSchema, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=error_response(message=messages.TASK_NOT_FOUND, status_code=404))

    task.title = body.title
    task.description = body.description
    task.due_date = body.due_date
    task.completed = body.is_completed

    db.commit()
    db.refresh(task)
    return success_response(data=task, message=messages.TASK_UPDATED)

def delete_task(task_id: int, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=error_response(message=messages.TASK_NOT_FOUND, status_code=404))

    db.delete(task)
    db.commit()
    return success_response(message=messages.TASK_DELETED)