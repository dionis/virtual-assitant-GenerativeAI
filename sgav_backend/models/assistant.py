from datetime import datetime
from typing import Annotated, List
from pydantic import BaseModel, Field
from models.pydantic_oid import ObjectId, ObjectIdPydanticAnnotation


class Assistant(BaseModel):
    ID: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(
        alias="_id", default=None
    )
    name: str = Field(alias="name", default="")
    user_id: Annotated[ObjectId, ObjectIdPydanticAnnotation] | str = Field(
        alias="user_id", default=None
    )
    description: str = Field(alias="description", default="")
    knowledge: str = Field(alias="knowledge", default="")
    questions: List[str] = Field(alias="questions", default=list())
    answers: List[str] = Field(alias="answers", default=list())
    createdAt: datetime | None = Field(alias="created_at", default=None)


class Questions(BaseModel):
    questions: List[str] = Field(alias="questions", default=list())


class Answers(BaseModel):
    answers: List[str] = Field(alias="answers", default=list())


class QA(BaseModel):
    name: str = Field(alias="name", default="")
    questions: List[str] = Field(alias="questions", default=list())
    answers: List[str] = Field(alias="answers", default=list())


class UserEmail(BaseModel):
    email: str = Field(alias="email", default="")
