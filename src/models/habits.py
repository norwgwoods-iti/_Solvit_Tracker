from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime

from src.database import Base

from datetime import datetime

class HabitModel(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(default=None)
    date_created_habit: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    checking: Mapped[bool] = mapped_column(default=False)