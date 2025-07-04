from datetime import datetime
from logging import fatal
from uuid import UUID

from pydantic import BaseModel, Field


class TopicoUser(BaseModel):
    id: UUID = Field(description="Internal topico team user ID")
    minecraft_id: UUID  | None = Field(description="User minecraft account data")
    telegram_id: int
