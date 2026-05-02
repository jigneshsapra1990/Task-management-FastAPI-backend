from typing import Any
from fastapi import HTTPException
from pydantic import BaseModel


class ApiResponse(BaseModel):
    """Pydantic model representing the standard API response structure."""
    status: str
    status_code: int
    message: str | None = None
    access_token: str | None = None
    data: Any = None


class Keys:
    """Static keys for response status values."""
    SUCCESS = "success"
    ERROR = "error"


def api_response(
    success: bool = True,
    message: str | None = None,
    data: Any = None,
    status_code: int = 200,
    access_token: str | None = None
):
    """
    Build a unified API response.
    - success=True  → returns ApiResponse with status 'success'
    - success=False → raises HTTPException with status 'error'
    """
    response = ApiResponse(
        status=Keys.SUCCESS if success else Keys.ERROR,
        status_code=status_code,
        message=message,
        data=data,
        access_token=access_token
    )

    result = response.model_dump()

    # Remove access_token from response if not provided
    if access_token is None:
        result.pop("access_token")

    if not success:
        raise HTTPException(status_code=status_code, detail=result)

    return result
