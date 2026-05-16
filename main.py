"""
Модуль для запуска приложения FastAPI.
"""

from fastapi import FastAPI
from app.api.endpoints.v1.currency import router as currenct_router

app = FastAPI()
app.include_router(currenct_router, prefix="/v1", tags=["currency"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
