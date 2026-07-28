import contextlib

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from src.api import main_router
from src.api.dependencies import SessionDep
from database.function import update_database

from src.database import engine, new_session


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):

    scheduler = AsyncIOScheduler()

    scheduler.add_job(update_database, 'cron', hour=12, minute=59, args=[new_session])
    scheduler.start()

    yield

    scheduler.shutdown(wait=True)

    await engine.dispose()


app = FastAPI(
    title="Хуита",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любых адресов (удобно для локальной разработки)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Разрешает все заголовки
)


app.include_router(main_router)