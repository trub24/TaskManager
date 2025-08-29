import datetime
import enum
from typing import Annotated, Optional
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

str_256 = Annotated[str, 256]
created_at = Annotated[
    datetime.datetime, mapped_column(
        server_default=func.now()
        )
    ]


class Status(enum.Enum):
    pending = 'pending'
    in_progress = 'in_progress'
    done = 'done'


class Task(Base):
    title: Mapped[str_256]
    description: Mapped[Optional[str]]
    status: Mapped[Status]
    created_at: Mapped[created_at]
