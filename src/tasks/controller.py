from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel

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
    return {"message": "Create a new task"}


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return tasks    


def get_task(task_id: int, db:Session):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    return task