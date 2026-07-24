from fastapi import Form, APIRouter

from typing import Annotated

from sqlalchemy import select

from src.api.function import get_habit_function
from src.database import engine, Base
from src.api.dependencies import SessionDep
from src.models.habits import HabitModel
from src.schemas.habits import HabitAddSchema, HabitSchema

router = APIRouter()


""" POST """
@router.post("/setup_database",
          tags=["Установка Базы Данных 💽"],
          summary="Установить БД")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        print('База Данных деактивирована')
        await conn.run_sync(Base.metadata.create_all)
        print('База данных создана')
    return {
        "ok": True,
    }


""" POST """
@router.post("/habits",
          tags=["Привычки 🚬"],
          summary='Добавить новую привычку')
async def post_habits(habit: HabitAddSchema, session: SessionDep):
    new_habit = HabitModel(
        name=habit.name,
        description=habit.description
    )
    session.add(new_habit)
    await session.commit()

    return {
        "ok": True,
    }


""" GET """
@router.get("/habits",
         tags=["Привычки 🚬"],
         summary="Получить список всех привычек")
async def get_habits(session: SessionDep) -> list[HabitSchema]:
    # query = select(HabitModel)  # Создаем запрос
    # result = await session.execute(query)  # Отправляем запрос
    # habits = result.scalars().all()  # Получаем все запси

    habits = await session.scalars(select(HabitModel))

    return habits.all()


""" GET """
@router.get("/habits/{habit_id}",
          tags=["Привычки 🚬"],
         summary="Получить привычку по ID")
async def get_habits(habit_id: int, session: SessionDep) -> HabitSchema:

    return await get_habit_function(session=session, id=habit_id, model=HabitModel)



""" UPDATE """
@router.put("/habits/{habit_id}",
          tags=["Привычки 🚬"],
         summary="Обновить данные привычки по ID")
async def update_habits(habit_id: int, habit_data: HabitAddSchema, session: SessionDep):

    habit = await get_habit_function(session=session, id=habit_id, model=HabitModel)

    habit.name = habit_data.name
    habit.description = habit_data.description

    await session.commit()
    await session.refresh(habit)

    return {
        "ok": True,
    }


""" PATCH Toggle """
@router.patch("/habits/{habit_id}/toggle",
              tags=["Привычки 🚬"],
              summary="Обновить Статус 'Выполнено' по ID")
async def toggle_habit(habit_id: int, session: SessionDep):

    habit = await get_habit_function(session=session, id=habit_id, model=HabitModel)

    habit.checking = not habit.checking

    await session.commit()
    await session.refresh(habit)

    return {
        "ok": True,
        "checking": habit.checking
    }


""" DELETE """
@router.delete("/habits/{habit_id}",
          tags=["Привычки 🚬"],
        summary="Удалить привычку")
async def delete_habit(habit_id: int, session: SessionDep):

    habit = await get_habit_function(session=session, id=habit_id, model=HabitModel)

    await session.delete(habit)
    await session.commit()

    return {
        "ok": True,
    }