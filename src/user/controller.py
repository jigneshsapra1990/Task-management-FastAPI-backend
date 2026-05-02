from sqlalchemy.orm import Session
from src.user.dtos import UserSchema, UserLoginSchema
from src.user.models import UserModel
from src.utils.Keys import Keys
from src.utils.Messages import messages
from src.utils.response import api_response
from src.utils.constant import status_code
from pwdlib import PasswordHash
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta

password_hash = PasswordHash.recommended()


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)

def register_user(body: UserSchema, db: Session):
    """Register a new user in the database."""
    # Check if user with the same email already exists
    existing_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if existing_user:
        api_response(success=False, message=messages.User_ALREADY_EXISTS, status_code=status_code.BAD_REQUEST)

    # Check if user with the same username already exists
    existing_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    if existing_username:
        api_response(success=False, message=messages.Username_ALREADY_EXISTS, status_code=status_code.BAD_REQUEST)

    hashed_password = get_password_hash(body.password)
    new_user = UserModel(
        username=body.username,
        email=body.email,
        password=hashed_password,
        name=body.name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({Keys.USER_ID: new_user.id, Keys.EXPIRES: str(expires_delta)}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return api_response(message=messages.User_REGISTERED, data=new_user.to_dict(), access_token=token, status_code=status_code.CREATED)


def login_user(body: UserLoginSchema, db: Session):
    """Authenticate a user and return their details if successful."""
    user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if user is None:
        api_response(success=False, message=messages.User_NOT_FOUND, status_code=status_code.NOT_FOUND)

    if not verify_password(body.password, user.password):
        api_response(success=False, message=messages.User_NOT_FOUND, status_code=status_code.NOT_FOUND)

    expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({Keys.USER_ID: user.id, Keys.EXPIRES: str(expires_delta)}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return api_response(message=messages.User_LOGGED_IN, data=user.to_dict(), access_token=token, status_code=status_code.OK)
