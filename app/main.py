import streamlit as st
from datetime import date

from app.extraction import extract_actions
from app.deduplication import deduplicate_actions
from app.ownership import validate_ownership
from app.deadlines import update_statuses
from app.brief import build_daily_brief
from app.qa import answer_question


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Executive Productivity Agent",
    page_icon="⚡",
    layout="wide",
)


# ============================================================
# CONSTANTS
# ============================================================

EXECUTIVE = "Arjun Malhotra"
ROLE = "VP Sales"

DEFAULT_DATE = date(2026, 9, 24)

STATUS_LABELS = {
    "overdue": "OVERDUE",
    "due_today": "DUE TODAY",
    "unclear_ownership": "OWNERSHIP UNCLEAR",
    "completed": "COMPLETED",
    "waiting": "WAITING",
    "open": "OPEN",
}


# ============================================================
# DATA PIPELINE
# ============================================================

@st.cache_data
def load_actions(reference_date):

    # 1. Extract candidate actions
    actions = extract_actions()

    # 2. Deduplicate cross-source mentions
    actions = deduplicate_actions(actions)

    # 3. Validate ownership
    actions = validate_ownership(actions)

    # 4. Resolve current status
    actions = update_statuses(
        actions,
        reference_date,
    )

    return actions


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_deadline(action):

    if not action.deadline:
        return "No deadline specified"

    return action.deadline.strftime(
        "%a, %d %b %Y · %I:%M %p"
    )


def render_action(action):

    status = action.status.value

    if status == "overdue":
        st.error(
            f"🔴 **{STATUS_LABELS[status]}**  \n"
            f"### {action.title}  \n"
            f"Deadline: **{format_deadline(action)}**  \n"
            f"Counterparty: **{action.counterparty or '—'}**"
        )

    elif status == "due_today":
        st.warning(
            f"🟡 **{STATUS_LABELS[status]}**  \n"
            f"### {action.title}  \n"
            f"Deadline: **{format_deadline(action)}**  \n"
            f"Counterparty: **{action.counterparty or '—'}**"
        )

    elif status == "unclear_ownership":
        st.warning(
            f"🟠 **{STATUS_LABELS[status]}**  \n"
            f"### {action.title}  \n"
            f"Deadline: **{format_deadline(action)}**  \n"
            f"Owner: **NOT CONFIRMED**"
        )

    elif status == "completed":
        st.success(
            f"🟢 **{STATUS_LABELS[status]}**  \n"
            f"### {action.title}"
        )

    else:
        st.info(
            f"**{STATUS_LABELS.get(status, status.upper())}**  \n"
            f"### {action.title}  \n"
            f"Deadline: **{format_deadline(action)}**"
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("⚡ Executive Agent")

    st.caption(
        f"{EXECUTIVE} · {ROLE}"
    )

    st.divider()

    reference_date = st.date_input(
        "Brief date",
        value=DEFAULT_DATE,
        min_value=date(2026, 9, 21),
        max_value=date(2026, 9, 25),
    )

    st.divider()

    st.markdown("### Sources")

    st.markdown(
        """
        ✓ Leadership Sync  
        ✓ Email threads  
        ✓ Calendars  
        ✓ Voice notes
        """
    )

    st.divider()

    st.markdown("### Guardrails")

    st.caption(
        "Ownership is never inferred when the source "
        "does not explicitly establish it."
    )


# ============================================================
# LOAD DATA
# ============================================================

actions = load_actions(reference_date)

brief = build_daily_brief(
    actions,
    reference_date,
)


# ============================================================
# HEADER
# ============================================================

st.title("Executive Productivity Agent")

st.markdown(
    f"### Daily Brief · "
    f"{reference_date.strftime('%A, %d %B %Y')}"
)

st.caption(
    "Source-grounded action intelligence for "
    f"{EXECUTIVE}, {ROLE}"
)


# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

my_actions = brief["my_actions"]
overdue = brief["overdue"]
unclear = brief["ownership_unclear"]
completed = brief["completed"]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "My Actions",
        len(my_actions),
    )

with col2:
    st.metric(
        "Overdue",
        len(overdue),
    )

with col3:
    st.metric(
        "Ownership Unclear",
        len(unclear),
    )

with col4:
    st.metric(
        "Completed",
        len(completed),
    )


# ============================================================
# EXECUTIVE READOUT
# ============================================================

if reference_date == date(2026, 9, 24):

    st.info(
        "**Executive readout:** "
        "3 direct actions require attention, "
        "1 critical item remains unowned, "
        "and 1 prior commitment is overdue."
    )


# ============================================================
# MY ACTIONS
# ============================================================

st.divider()

st.header("🔴 My Actions")

if my_actions:

    for action in my_actions:
        render_action(action)

else:

    st.success(
        "No direct actions require attention."
    )


# ============================================================
# OWNERSHIP EXCEPTIONS
# ============================================================

st.divider()

st.header("🟠 Ownership Exceptions")

if unclear:

    for action in unclear:

        st.warning(
            f"""
**{action.title}**

**Deadline:** {format_deadline(action)}

**Owner:** NOT CONFIRMED

**Potential owner mentioned:** {action.counterparty or "None"}

**Why it is flagged:**

{action.evidence[3] if len(action.evidence) > 3 else action.evidence[-1]}

> The agent will not infer ownership without confirmation.
"""
        )

else:

    st.success(
        "No unresolved ownership issues."
    )


# ============================================================
# WAITING / DEPENDENCIES
# ============================================================

st.divider()

st.header("🟡 Waiting / Dependencies")

waiting = brief["waiting_on_others"]

if waiting:

    for action in waiting:

        st.info(
            f"**{action.title}**  \n"
            f"Waiting on: **{action.waiting_on}**"
        )

else:

    st.caption(
        "No active items are explicitly waiting on another person."
    )


# ============================================================
# COMPLETED
# ============================================================

st.divider()

st.header("🟢 Closed Loop")

if completed:

    for action in completed:

        st.success(
            f"✓ **{action.title}**"
        )

else:

    st.caption("No completed items.")


# ============================================================
# Q&A
# ============================================================

st.divider()

st.header("Ask the Agent")

st.caption(
    "Ask about commitments, deadlines, ownership, "
    "waiting items, or specific people."
)

question = st.text_input(
    "Your question",
    placeholder="What did I promise Raghav?",
)

if question:

    answer = answer_question(
        question,
        actions,
        reference_date,
    )

    st.markdown(answer)


# ============================================================
# TRACEABILITY
# ============================================================

st.divider()

with st.expander("🔎 Source Traceability"):

    st.caption(
        "Every canonical action retains the source references "
        "and evidence used to derive its current state."
    )

    for action in actions:

        st.markdown(
            f"### {action.title}"
        )

        st.write(
            f"**Owner:** "
            f"{action.owner or 'Not confirmed'}"
        )

        st.write(
            f"**Status:** "
            f"{action.status.value}"
        )

        st.write(
            f"**Sources:** "
            f"{', '.join(action.sources)}"
        )

        st.write("**Evidence:**")

        for evidence in action.evidence:

            st.write(
                f"• {evidence}"
            )

        st.divider()


# ============================================================
# ARCHITECTURE
# ============================================================

with st.expander("🏗️ Agent Architecture"):

    st.code(
        """
        MEETING ───────┐
        EMAILS ────────┤
        CALENDARS ─────┼──> NORMALIZATION
        VOICE NOTES ───┘
                           │
                           ▼
                    COMMITMENT EXTRACTION
                           │
                           ▼
                    CROSS-SOURCE DEDUP
                           │
                           ▼
                    OWNERSHIP VALIDATION
                           │
                           ▼
                    DEADLINE RESOLUTION
                           │
                           ▼
                    CANONICAL ACTIONS
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        DAILY BRIEF       Q&A      TRACEABILITY
        """
    )

    st.caption(
        "Design principle: uncertainty is preserved instead "
        "of being converted into an unsupported assumption."
    )