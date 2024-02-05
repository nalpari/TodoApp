from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Users

router = APIRouter()


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str

    class Config:
        json_schema_extra = {
            'example': {
                'email': 'yoo32767@gmail.com',
                'username': 'yoo32767',
                'first_name': 'sangwook',
                'last_name': 'yoo',
                'password': 'password',
                'role': 'user'
            }
        }


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/auth")
async def get_user():
    return {"message": "Hello World"}


@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest, db: db_dependency):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=create_user_request.password,
        is_active=True,
    )

    return create_user_model
