# app/main.py

from fastapi import FastAPI
from app.routers import users
from app.exceptions.handlers import validation_exception_handler, sqlalchemy_exception_handler, http_exception_handler
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

app = FastAPI()

# Register exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

# Include routers
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Hello World"}
