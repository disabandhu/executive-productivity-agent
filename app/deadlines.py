from datetime import datetime, date
from typing import List

from app.models import Action, ActionStatus


def resolve_status(
    action: Action,
    reference_date: date
) -> ActionStatus:

    # Completed actions remain completed.
    if action.status == ActionStatus.COMPLETED:
        return ActionStatus.COMPLETED

    # Ownership uncertainty takes precedence.
    if not action.ownership_confirmed:
        return ActionStatus.UNCLEAR_OWNERSHIP

    if action.deadline is None:
        return ActionStatus.OPEN

    deadline_date = action.deadline.date()

    if deadline_date < reference_date:
        return ActionStatus.OVERDUE

    if deadline_date == reference_date:
        return ActionStatus.DUE_TODAY

    return ActionStatus.OPEN


def update_statuses(
    actions: List[Action],
    reference_date: date
) -> List[Action]:

    for action in actions:
        action.status = resolve_status(
            action,
            reference_date
        )

    return actions