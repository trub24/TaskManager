from typing import Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Task, Status

from src.api_v1.schemas import TaskCreate, TaskUpdate, TaskUpdatePartial


async def get_tasks(session: AsyncSession,
                    status: Optional[Status] = None) -> list[Task]:
    if status is None:
        stmt = select(Task).order_by(Task.created_at)
    else:
        stmt = select(Task).order_by(Task.created_at).filter(status == Task.status)
    result: Result = await session.execute(stmt)
    task = result.scalars().all()
    return list(task)


async def get_task(session: AsyncSession, task_id: int) -> Optional[Task]:
    return await session.get(Task, task_id)


async def create_task(session: AsyncSession, task_in: TaskCreate) -> Task:
    task = Task(**task_in.model_dump())
    session.add(task)
    await session.commit()
    return task


async def update_task(
    session: AsyncSession,
    task: Task,
    task_update: TaskUpdate | TaskUpdatePartial,
    partial: bool = False,
) -> Task:
    for name, value in task_update.model_dump(
        exclude_unset=partial
    ).items():
        setattr(task, name, value)
    await session.commit()
    return task


async def delete_task(
    session: AsyncSession,
    task: Task
) -> None:
    await session.delete(task)
    await session.commit()
