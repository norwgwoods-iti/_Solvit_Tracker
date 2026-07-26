from http.client import HTTPException

from testes import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime

from sqlalchemy.sql.annotation import Annotated
from starlette import status
from starlette.responses import Response


class HabitAddSchema(BaseModel):
    # name: str = Field(default='Название привычки', min_length=1, max_length=50)
    name: str
    description: str | None = Field(default='Необязательное поле', max_length=150)

    model_config = ConfigDict(from_attributes=True)


    @field_validator('name')
    def name_validator(cls, value):
        if value == 'Привет':
            raise ValueError('Недопустимое имя привычки')
        else:
            return value


class HabitSchema(HabitAddSchema):
    id: int = Field(frozen=True)
    date_created_habit: datetime = Field(frozen=True)
    checking: bool

    # model_config = ConfigDict(from_attributes=True, extra='forbid')

# class HabitUpdateSchema('?'):
#     pass