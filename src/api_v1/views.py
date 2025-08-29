from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from src.models import db_helper, Status
from src.api_v1 import crud
from src.api_v1.dependencies import task_by_id
from src.api_v1.schemas import Task, TaskCreate, TaskUpdate, TaskUpdatePartial

router = APIRouter(
    tags=['Tasks'],
)


@router.get('/tasks/', response_model=list[Task])
async def get_tasks(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    status: Optional[Status] = None
):
    return await crud.get_tasks(session=session, status=status)


@router.post(
    '/tasks/',
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_task(session=session, task_in=task_in)


@router.get('/tasks/{task_id}/', response_model=Task)
async def get_task(
    task: Task = Depends(task_by_id),
):
    return task


@router.put('/tasks/{task_id}/')
async def update_task(
    task_update: TaskUpdate,
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_task(
        session=session,
        task=task,
        task_update=task_update,
    )


@router.patch('/tasks/{task_id}/')
async def update_task_partial(
    task_update: TaskUpdatePartial,
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_task(
        session=session,
        task=task,
        task_update=task_update,
        partial=True,
    )


@router.delete('/tasks/{task_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_task(session=session, task=task)
