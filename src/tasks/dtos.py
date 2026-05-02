from pydantic import BaseModel

class TaskSchema(BaseModel):
    title: str
    description: str | None = None
    due_date: str | None = None 
    is_completed: bool = False