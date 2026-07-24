from fastapi.params import Depends
from typing import Annotated

from src.database import get_session

from sqlalchemy.ext.asyncio import AsyncSession

SessionDep = Annotated[AsyncSession, Depends(get_session)]
