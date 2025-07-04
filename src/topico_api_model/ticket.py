from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TicketCategory(BaseModel):
    id: UUID
    name: str
    description: str
    limit: int

class TicketMessage(BaseModel):
    """Ticket message model"""
    user_id: int = Field(description="Telegram user ID")
    message: str
    dt: datetime

class TicketAction(BaseModel):
    """Ticket action model. Example: Ticket closing"""
    user_id: int = Field(description="Telegram user ID")
    action: str

class Ticket(BaseModel):
    topic_id: int
    dt: datetime
    messages: list[TicketMessage]
    actions: list[TicketAction]