import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_get_tasks():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test'
    ) as ac:
        response = await ac.get('/api/v1/tasks/')
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_task():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url='http://test'
    ) as ac:
        response = await ac.post('/api/v1/tasks/', json={
            'title': 'test',
            'description': 'test',
            'status': 'done'
        }
        )
        assert response.status_code == 201
