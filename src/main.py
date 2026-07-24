from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api import main_router


app = FastAPI(
    title="Хуита"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любых адресов (удобно для локальной разработки)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Разрешает все заголовки
)


app.include_router(main_router)