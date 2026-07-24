from pydantic import BaseModel, ConfigDict
from datetime import datetime


class HabitAddSchema(BaseModel):
    name: str
    description: str | None = None

class HabitSchema(HabitAddSchema):
    id: int
    date_created_habit: datetime
    checking: bool = False

    model_config = ConfigDict(from_attributes=True)

# class HabitUpdateSchema('?'):
#     pass