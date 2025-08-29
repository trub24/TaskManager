from fastapi import FastAPI

import uvicorn

from src.core.config import settings
from src.api_v1.views import router as task_router

app = FastAPI()
app.include_router(router=task_router, prefix=settings.api_v1_prefix)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)
