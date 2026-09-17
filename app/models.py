from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ActionStatus(str, Enum):
    OPEN = "open"
    DUE_TODAY = "due_today"
    OVERDUE = "overdue"
    WAITING = "waiting"
    COMPLETED = "completed"
    UNCLEAR_OWNERSHIP = "unclear_ownership"


class Action(BaseModel):
    """
    Canonical representation of an executive action.

    Every source eventually gets normalized into this structure.
    """

    id: str

    title: str

    owner: Optional[str] = None

    counterparty: Optional[str] = None

    deadline: Optional[datetime] = None

    status: ActionStatus = ActionStatus.OPEN

    priority: str = "Medium"

    waiting_on: Optional[str] = None

    sources: list[str] = Field(default_factory=list)

    evidence: list[str] = Field(default_factory=list)

    ownership_confirmed: bool = True

    confidence: float = 1.0

    

    