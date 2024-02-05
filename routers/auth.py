from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Users
from passlib.context import CryptContext

router = APIRouter()


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


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


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return create_user_model
