from datetime import datetime
from typing import List

from app.models import Action, ActionStatus
from data.sources import MEETING_TRANSCRIPT, EMAIL_THREADS, VOICE_NOTES


def extract_actions() -> List[Action]:
    """
    Extract candidate actions from the supplied source data.

    In a production system, this layer would use an LLM/structured
    extraction model. For this controlled assignment dataset, we
    use deterministic extraction so every result is reproducible
    and traceable to the supplied evidence.
    """

    actions = []

    # ---------------------------------------------------------
    # 1. Vendor list
    # ---------------------------------------------------------
    actions.append(
        Action(
            id="vendor_list",
            title="Send updated vendor list to Raghav",
            owner="Arjun",
            counterparty="Raghav",
            deadline=datetime(2026, 9, 23, 9, 0),
            status=ActionStatus.OVERDUE,
            priority="High",
            sources=[
                "Leadership Sync",
                "Email: Vendor List",
                "Voice Note 1",
            ],
            evidence=[
                "Arjun said he would send Raghav the updated vendor list.",
                "Arjun later committed to Wednesday morning.",
                "Raghav followed up Wednesday at 8:45 AM asking if it was still good for that morning.",
            ],
            ownership_confirmed=True,
            confidence=1.0,
        )
    )

    # ---------------------------------------------------------
    # 2. Q3 campaign deck review
    # ---------------------------------------------------------
    actions.append(
        Action(
            id="campaign_deck_review",
            title="Review Q3 campaign deck with Neha",
            owner="Arjun",
            counterparty="Neha",
            deadline=datetime(2026, 9, 24, 9, 30),
            status=ActionStatus.DUE_TODAY,
            priority="High",
            waiting_on=None,
            sources=[
                "Leadership Sync",
                "Email: Q3 Campaign Deck",
                "Arjun Calendar",
            ],
            evidence=[
                "Neha initially targeted Wednesday for the review.",
                "Neha moved the review to Thursday morning.",
                "Arjun agreed to Thursday morning.",
                "Neha confirmed 9:30 AM Thursday and sent the deck at 8:00 AM.",
            ],
            ownership_confirmed=True,
            confidence=1.0,
        )
    )

    # ---------------------------------------------------------
    # 3. Expense variance report
    # ---------------------------------------------------------
    actions.append(
        Action(
            id="expense_variance_review",
            title="Review July expense variance report before board prep",
            owner="Arjun",
            counterparty="Divya",
            deadline=datetime(2026, 9, 24, 9, 0),
            status=ActionStatus.DUE_TODAY,
            priority="High",
            waiting_on=None,
            sources=[
                "Leadership Sync",
                "Email: Expense Variance Report",
                "Voice Note 2",
            ],
            evidence=[
                "Arjun asked Divya for the July expense variance report.",
                "Arjun requested Wednesday evening instead of Thursday morning.",
                "Divya delivered the report Wednesday at 6:00 PM.",
                "Arjun said he needed it before Thursday board prep.",
            ],
            ownership_confirmed=True,
            confidence=1.0,
        )
    )

    # ---------------------------------------------------------
    # 4. Mumbai lease ownership
    # ---------------------------------------------------------
    actions.append(
        Action(
            id="mumbai_lease_ownership",
            title="Resolve ownership of Mumbai office lease renewal signature",
            owner=None,
            counterparty="Facilities",
            deadline=datetime(2026, 9, 25, 17, 0),
            status=ActionStatus.UNCLEAR_OWNERSHIP,
            priority="Critical",
            waiting_on="Internal owner",
            sources=[
                "Leadership Sync",
                "Email: Mumbai Office Lease Renewal",
                "Voice Note 1",
            ],
            evidence=[
                "The lease requires an authorized signature by Friday.",
                "Raghav asked who was signing off.",
                "Divya said she believed this typically sits with Facilities.",
                "No source confirms that Facilities has actually been assigned.",
                "Arjun explicitly said: flag it, don't assume.",
            ],
            ownership_confirmed=False,
            confidence=1.0,
        )
    )

    # ---------------------------------------------------------
    # 5. Meridian Logistics call
    # ---------------------------------------------------------
    actions.append(
        Action(
            id="meridian_call",
            title="Reconfirm / lock Meridian Logistics call time with Priya",
            owner="Arjun",
            counterparty="Priya",
            deadline=datetime(2026, 9, 23, 15, 0),
            status=ActionStatus.COMPLETED,
            priority="Medium",
            sources=[
                "Leadership Sync",
                "Email: Call Reschedule",
                "Arjun Calendar",
                "Voice Note 2",
            ],
            evidence=[
                "Arjun said he needed to reconfirm the new time himself.",
                "Arjun proposed Wednesday at 3:00 PM.",
                "Priya confirmed Wednesday at 3:00 PM.",
                "Arjun reconfirmed the call at 2:00 PM Wednesday.",
                "The calendar contains the Wednesday 3:00 PM Meridian call.",
            ],
            ownership_confirmed=True,
            confidence=1.0,
        )
    )

    return actions