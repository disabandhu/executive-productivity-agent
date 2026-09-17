from typing import List

from app.models import Action


def deduplicate_actions(actions: List[Action]) -> List[Action]:
    """
    Merge multiple mentions of the same underlying action.

    Actions are grouped by their canonical ID. In a production
    implementation this could be backed by semantic similarity /
    embeddings, but the important business behavior is that one
    real-world commitment becomes one canonical action.
    """

    merged = {}

    for action in actions:
        if action.id not in merged:
            merged[action.id] = action
            continue

        existing = merged[action.id]

        # Merge source references.
        existing.sources = list(
            dict.fromkeys(existing.sources + action.sources)
        )

        # Merge evidence.
        existing.evidence = list(
            dict.fromkeys(existing.evidence + action.evidence)
        )

        # Prefer an explicitly confirmed owner.
        if not existing.ownership_confirmed and action.ownership_confirmed:
            existing.owner = action.owner
            existing.ownership_confirmed = True

        # Prefer the latest known deadline when available.
        if action.deadline and (
            existing.deadline is None
            or action.deadline > existing.deadline
        ):
            existing.deadline = action.deadline

        merged[action.id] = existing

    return list(merged.values())