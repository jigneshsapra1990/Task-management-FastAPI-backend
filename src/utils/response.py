from pydantic import BaseModel
from src.utils.Keys import keys
from typing import Any

class ApiResponse(BaseModel):
    status: str
    status_code: int
    message: str | None = None
    data: Any = None

def success_response(data=None, message=None, status_code=200):
    return {
        keys.STATUS: keys.SUCCESS,
        keys.STATUS_CODE: status_code,
        keys.MESSAGE: message,
        keys.DATA: data
    }

def error_response(message=None, status_code=400):
    return {
        keys.STATUS: keys.ERROR,
        keys.STATUS_CODE: status_code,
        keys.MESSAGE: message,
        keys.DATA: None
    }
