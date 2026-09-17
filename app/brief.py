from datetime import date
from typing import List, Dict

from app.models import Action, ActionStatus


def build_daily_brief(
    actions: List[Action],
    reference_date: date
) -> Dict[str, List[Action]]:
    """
    Organize canonical actions into an executive-friendly daily brief.
    """

    brief = {
        "my_actions": [],
        "waiting_on_others": [],
        "overdue": [],
        "ownership_unclear": [],
        "completed": [],
    }

    for action in actions:

        if action.status == ActionStatus.COMPLETED:
            brief["completed"].append(action)

        elif action.status == ActionStatus.OVERDUE:
            if action.owner == "Arjun":
                brief["my_actions"].append(action)

            brief["overdue"].append(action)

        elif action.status == ActionStatus.DUE_TODAY:
            if action.owner == "Arjun":
                brief["my_actions"].append(action)

            elif action.waiting_on:
                brief["waiting_on_others"].append(action)

        elif action.status == ActionStatus.WAITING:
            brief["waiting_on_others"].append(action)

        elif action.status == ActionStatus.UNCLEAR_OWNERSHIP:
            brief["ownership_unclear"].append(action)

    return brief