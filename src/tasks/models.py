from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase
from src.utils.Tables import tables
from src.utils.Keys import Keys

class Base(DeclarativeBase):
    pass

class TaskModel(Base):
    __tablename__ = tables.TASKS

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=True)
    completed = Column(Boolean, default=False)

    def to_dict(self):
        return {
            Keys.ID: self.id,
            Keys.TITLE: self.title,
            Keys.DESCRIPTION: self.description,
            Keys.DUE_DATE: str(self.due_date) if self.due_date else None,
            Keys.COMPLETED: self.completed
        }
