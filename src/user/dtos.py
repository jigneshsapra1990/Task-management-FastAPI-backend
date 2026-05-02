from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    name: str

class UserLoginSchema(BaseModel):
    email: str
    password: str    