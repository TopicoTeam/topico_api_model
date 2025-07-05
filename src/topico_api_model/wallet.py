from datetime import datetime
from logging import fatal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

class Wallet(BaseModel):
    id: UUID
    amount: int

class Transaction(BaseModel):
    id: UUID
    amount: int
    from_id: UUID
    to_id: UUID
    dt: datetime