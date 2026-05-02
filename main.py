from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from src.utils.db import engine
from src.tasks.models import Base, TaskModel
from src.tasks.router import tasks_router
from src.user.router import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")
app.include_router(tasks_router)
app.include_router(user_routes)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content=exc.detail)

