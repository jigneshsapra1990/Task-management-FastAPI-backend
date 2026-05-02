from fastapi import APIRouter, Depends, Request
from src.user import controller
from src.user.dtos import UserSchema, UserLoginSchema
from src.utils.db import get_db
from src.utils.constant import routes, status_code
from sqlalchemy.orm import Session

user_routes = APIRouter(prefix="/users", tags=["users"])

# Register a new user
@user_routes.post(routes.CREATER_USER, status_code=status_code.CREATED)
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register_user(body, db)

# Login user
@user_routes.post(routes.LOGIN_USER, status_code=status_code.OK)
def login_user(body: UserLoginSchema, db: Session = Depends(get_db)):
    return controller.login_user(body, db)

# IsAuthenticated route
@user_routes.get(routes.IS_AUTHENTICATED, status_code=status_code.OK)
def is_authenticated(request: Request, db: Session = Depends(get_db)):
    return controller.is_authenticated(request, db)
