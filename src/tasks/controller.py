from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.utils.Messages import messages

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
    return {"message": messages.TASK_CREATED}


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return tasks


def get_task(task_id: int, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=messages.TASK_NOT_FOUND)
    return task

def update_task(task_id: int, body: TaskSchema, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=messages.TASK_NOT_FOUND)

    task.title = body.title
    task.description = body.description
    task.due_date = body.due_date
    task.completed = body.is_completed

    db.commit()
    db.refresh(task)
    return {"message": messages.TASK_UPDATED}

def delete_task(task_id: int, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail=messages.TASK_NOT_FOUND)

    db.delete(task)
    db.commit()
    return {"message": messages.TASK_DELETED}