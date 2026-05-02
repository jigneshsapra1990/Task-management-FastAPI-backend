from pydantic import BaseModel
from pydantic import ConfigDict

class TaskSchema(BaseModel):
    title: str
    description: str | None = None
    due_date: str | None = None
    is_completed: bool = False

class TaskResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    due_date: str | None = None
    completed: bool = False
