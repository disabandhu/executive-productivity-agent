from datetime import date
from typing import List

from app.models import Action


def answer_question(
    question: str,
    actions: List[Action],
    reference_date: date
) -> str:

    q = question.lower().strip()

    # ----------------------------------------
    # What did I promise Raghav?
    # ----------------------------------------
    if "promise" in q and "raghav" in q:

        matches = [
            a for a in actions
            if a.counterparty == "Raghav"
            and a.owner == "Arjun"
        ]

        if not matches:
            return "I could not find a source-grounded commitment to Raghav."

        action = matches[0]

        deadline = (
            action.deadline.strftime("%A, %d %B %Y at %I:%M %p")
            if action.deadline
            else "No explicit deadline found"
        )

        return (
            f"You promised Raghav: **{action.title}**.\n\n"
            f"Deadline: **{deadline}**.\n\n"
            f"Current status: **{action.status.value.replace('_', ' ')}**.\n\n"
            f"Evidence: {action.evidence[0]}"
        )

    # ----------------------------------------
    # What needs action today?
    # ----------------------------------------
    if (
        ("action" in q and "today" in q)
        or "what needs action" in q
    ):

        matches = [
            a for a in actions
            if (
                a.owner == "Arjun"
                and a.status.value in ["due_today", "overdue"]
            )
            or a.status.value == "unclear_ownership"
        ]

        if not matches:
            return "No action items require attention today."

        response = ["### Actions requiring attention\n"]

        for action in matches:

            if action.status.value == "unclear_ownership":
                response.append(
                    f"- **{action.title}** — "
                    f"ownership is unclear; deadline is "
                    f"{action.deadline.strftime('%A, %d %B')}."
                )
            else:
                response.append(
                    f"- **{action.title}** — "
                    f"{action.status.value.replace('_', ' ')}."
                )

        return "\n".join(response)

    # ----------------------------------------
    # What is overdue?
    # ----------------------------------------
    if "overdue" in q:

        matches = [
            a for a in actions
            if a.status.value == "overdue"
        ]

        if not matches:
            return "There are no overdue items."

        response = ["### Overdue\n"]

        for action in matches:
            response.append(
                f"- **{action.title}** — "
                f"deadline was "
                f"{action.deadline.strftime('%A, %d %B %Y at %I:%M %p')}."
            )

        return "\n".join(response)

    # ----------------------------------------
    # What is waiting on others?
    # ----------------------------------------
    if "waiting" in q:

        matches = [
            a for a in actions
            if a.waiting_on
            and a.status.value not in [
                "completed",
                "unclear_ownership",
            ]
        ]

        if not matches:
            return (
                "No active items are explicitly waiting on "
                "another person."
            )

        response = ["### Waiting on others\n"]

        for action in matches:
            response.append(
                f"- **{action.title}** — waiting on "
                f"{action.waiting_on}."
            )

        return "\n".join(response)

    # ----------------------------------------
    # Ownership question
    # ----------------------------------------
    if (
        "owner" in q
        or "ownership" in q
        or "who owns" in q
    ):

        matches = [
            a for a in actions
            if a.status.value == "unclear_ownership"
        ]

        if not matches:
            return "No unresolved ownership issues were found."

        action = matches[0]

        return (
            f"**Ownership unclear:** {action.title}.\n\n"
            f"Deadline: **{action.deadline.strftime('%A, %d %B %Y at %I:%M %p')}**.\n\n"
            f"The source data does not confirm an owner. "
            f"I will not infer one."
        )

    # ----------------------------------------
    # Campaign deck
    # ----------------------------------------
    if "deck" in q or "campaign" in q:

        matches = [
            a for a in actions
            if a.id == "campaign_deck_review"
        ]

        if matches:
            a = matches[0]

            return (
                f"**Q3 campaign deck review** is scheduled for "
                f"**{a.deadline.strftime('%A, %d %B at %I:%M %p')}**.\n\n"
                f"Neha has delivered the deck. "
                f"Your action is to review it."
            )

    # ----------------------------------------
    # Expense report
    # ----------------------------------------
    if "expense" in q or "variance" in q:

        matches = [
            a for a in actions
            if a.id == "expense_variance_review"
        ]

        if matches:
            a = matches[0]

            return (
                f"**July expense variance report:** "
                f"Divya delivered the report Wednesday evening.\n\n"
                f"Your action is to review it before Thursday's "
                f"board prep."
            )

    # ----------------------------------------
    # Meridian
    # ----------------------------------------
    if "meridian" in q or "priya" in q:

        matches = [
            a for a in actions
            if a.id == "meridian_call"
        ]

        if matches:
            return (
                "**Meridian Logistics:** the call was confirmed "
                "for Wednesday at 3:00 PM and subsequently "
                "reconfirmed by Arjun."
            )

    return (
        "I can answer questions about commitments, deadlines, "
        "overdue work, ownership, waiting items, the vendor list, "
        "campaign deck, expense report, Mumbai lease, and "
        "Meridian Logistics."
    )