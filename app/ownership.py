from typing import List

from app.models import Action


def validate_ownership(actions: List[Action]) -> List[Action]:
    """
    Validate ownership without inventing an owner.

    If no confirmed owner exists in the source data,
    ownership remains unresolved.
    """

    for action in actions:

        if not action.owner:
            action.ownership_confirmed = False
            continue

        action.ownership_confirmed = True

    return actions