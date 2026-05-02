from fastapi import Depends, Request
from sqlalchemy.orm import Session
from src.user.models import UserModel
from src.utils.Keys import Keys
from src.utils.Messages import messages
from src.utils.db import get_db
from src.utils.response import api_response
from src.utils.constant import status_code
from src.utils.settings import settings
from datetime import datetime
import jwt


def is_authenticated(request: Request, db: Session=Depends(get_db)):
    """Verify JWT token and return authenticated user details."""
    auth_header = request.headers.get("Authorization")

    if auth_header is None or not auth_header.startswith("jwt "):
        api_response(success=False, message=messages.User_UNAUTHORIZED, status_code=status_code.UNAUTHORIZED)

    token = auth_header.split(" ")[1]

    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.InvalidTokenError:
        api_response(success=False, message=messages.User_UNAUTHORIZED, status_code=status_code.UNAUTHORIZED)

    user_id = data.get(Keys.USER_ID)
    exp_time = data.get(Keys.EXPIRES)

    current_time = datetime.now().timestamp()

    if current_time > exp_time:
        api_response(success=False, message=messages.User_UNAUTHORIZED, status_code=status_code.UNAUTHORIZED)

    if user_id is None:
        api_response(success=False, message=messages.User_UNAUTHORIZED, status_code=status_code.UNAUTHORIZED)

    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if user is None:
        api_response(success=False, message=messages.User_NOT_FOUND, status_code=status_code.NOT_FOUND)

    return api_response(message=messages.User_AUTHENTICATED, data=user.to_dict(), status_code=status_code.OK)
