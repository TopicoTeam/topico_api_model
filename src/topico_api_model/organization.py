from datetime import datetime
from logging import fatal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

class Organization(BaseModel):
    id: UUID
    name: str
    description: str | None
    avatar_url: str | None
    is_closed: bool