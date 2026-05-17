"""
Модуль для запуска приложения FastAPI.
"""

from fastapi import FastAPI

from app.api.endpoints.v1.currency import router as currency_router
from app.api.endpoints.v1.users import router as users_router

app = FastAPI()
app.include_router(currency_router, prefix="/api/v1", tags=["currency"])
app.include_router(users_router, prefix="/api/v1", tags=["users"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
