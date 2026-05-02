from sqlalchemy import Column, Integer, String
from src.utils.db import Base
from src.utils.Tables import tables
from src.utils.Keys import Keys

class UserModel(Base):
    __tablename__ = tables.USERS

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)

    def to_dict(self):
        return {
            Keys.ID: self.id,
            Keys.NAME: self.name,
            Keys.EMAIL: self.email,
            Keys.USERNAME: self.username
        }