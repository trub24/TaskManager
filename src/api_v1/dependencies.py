from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper, Task

from src.api_v1 import crud

from uuid import UUID


async def task_by_id(
    task_id: Annotated[UUID, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Task:
    task = await crud.get_task(session=session, task_id=task_id)
    if task is not None:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Task{task_id} not found!',
    )
