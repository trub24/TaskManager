from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional
from src.models import Status
from uuid import UUID


class TaskBase(BaseModel):
    title: str
    description: Optional[str]


class TaskCreate(TaskBase):
    status: Status


class TaskUpdate(TaskCreate):
    pass


class TaskUpdatePartial(TaskBase):
    title: str | None = None
    description: str | None = None
    status: Status | None = None


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: Status
    created_at: datetime
