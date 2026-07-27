from starlette import status
from starlette.responses import Response

from src.models.habits import CheckinHabitModel


async def get_habit_function(session, model, id):
    habit = await session.get(model, id)

    if not habit:
        return Response(
            status_code=status.HTTP_404_NOT_FOUND,
            content=f'Habit with ID={id} not found'
        )

    return habit

# async def add_habit_in_table_checkins(habit, session):
#
#     new_checkin = CheckinHabitModel(
#         id=habit.id,
#         id_habit=habit.id_habit,
#         checkins_date=habit.checkins_date
#     )
#
#     session.add(new_checkin)