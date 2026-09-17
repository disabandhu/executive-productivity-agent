"""
Source data for the Executive Productivity Agent.

This file contains only the information supplied in the
assignment data pack.
"""

MEETING_TRANSCRIPT = """
Leadership Sync
Monday 21 September 2026
9:00–9:35 AM

Arjun: Let’s keep this quick. Neha, where are we on the Q3 campaign deck?

Neha: Draft is 80% done. I’ll send it to Arjun for review by Wednesday.

Arjun: Good. Also, remind me — I told Raghav I’d send him the updated vendor list.
I’ll get that to him by end of day tomorrow.

Raghav: Appreciated.

Raghav: Separately, the Mumbai office renewal paperwork needs someone to sign off
this week. Not sure whose desk that’s on right now.

Divya: I think that’s supposed to be Facilities, but I haven’t seen anyone pick it up.

Arjun: Okay, flag it, don’t assume.

Arjun: Divya, can you also pull the July expense variance report before Thursday’s
board prep?

Divya: Yes, I’ll have it ready Wednesday evening.

Arjun: One more thing — client call with Meridian Logistics got pushed.
I need to reconfirm the new time with their team myself.

Neha: Also, just a reminder, the campaign deck review — I said Wednesday,
but realistically Thursday morning is safer.

Arjun: Noted.
"""


EMAIL_THREADS = [
    {
        "thread": "Vendor List",
        "messages": [
            (
                "2026-09-21 09:50",
                "Raghav",
                "Arjun",
                "Following up from the sync — can you send the updated vendor list today?"
            ),
            (
                "2026-09-21 17:40",
                "Arjun",
                "Raghav",
                "Running behind, will send first thing tomorrow morning instead."
            ),
            (
                "2026-09-22 09:15",
                "Raghav",
                "Arjun",
                "No worries, whenever you get a chance today works."
            ),
            (
                "2026-09-22 18:30",
                "Arjun",
                "Raghav",
                "Sorry, got pulled into board prep — will send by tomorrow (Wednesday) morning for sure."
            ),
            (
                "2026-09-23 08:45",
                "Raghav",
                "Arjun",
                "Just checking — still good for this morning?"
            ),
        ],
    },
    {
        "thread": "Q3 Campaign Deck",
        "messages": [
            (
                "2026-09-21 11:00",
                "Neha",
                "Arjun",
                "Deck’s coming together, still targeting Wednesday for your review."
            ),
            (
                "2026-09-22 16:15",
                "Neha",
                "Arjun",
                "Heads up — shifting the review to Thursday morning instead of Wednesday, need one more day on the data slides."
            ),
            (
                "2026-09-23 10:00",
                "Arjun",
                "Neha",
                "Understood, Thursday morning works. What time exactly?"
            ),
            (
                "2026-09-23 10:20",
                "Neha",
                "Arjun",
                "Let’s say 9:30 AM Thursday, before your board prep block."
            ),
            (
                "2026-09-24 08:00",
                "Neha",
                "Arjun",
                "Deck is ready, attaching the draft ahead of our 9:30 review."
            ),
        ],
    },
    {
        "thread": "Call Reschedule",
        "messages": [
            (
                "2026-09-21 13:00",
                "Priya",
                "Arjun",
                "Our scheduled call this week got bumped from our side — can you propose a new time? We’re flexible Tuesday–Thursday afternoons."
            ),
            (
                "2026-09-22 15:00",
                "Arjun",
                "Priya",
                "Apologies for the delay — how about Wednesday 3:00 PM?"
            ),
            (
                "2026-09-22 17:45",
                "Priya",
                "Arjun",
                "Wednesday 3 PM works on our end, confirmed."
            ),
            (
                "2026-09-23 13:30",
                "Priya",
                "Arjun",
                "Quick check — still on for 3 PM today?"
            ),
            (
                "2026-09-23 14:00",
                "Arjun",
                "Priya",
                "Yes, confirmed, see you at 3."
            ),
        ],
    },
    {
        "thread": "Expense Variance Report",
        "messages": [
            (
                "2026-09-21 14:30",
                "Divya",
                "Arjun",
                "Starting on the July variance numbers, targeting Thursday morning for board prep as discussed."
            ),
            (
                "2026-09-22 09:00",
                "Arjun",
                "Divya",
                "Actually, can I get it by Wednesday evening instead? Want time to review before Thursday."
            ),
            (
                "2026-09-22 09:40",
                "Divya",
                "Arjun",
                "Wednesday evening is tight but doable, I’ll prioritize it."
            ),
            (
                "2026-09-23 18:00",
                "Divya",
                "Arjun",
                "Report attached, sent as promised."
            ),
            (
                "2026-09-23 18:10",
                "Arjun",
                "Divya",
                "Got it, thank you — exactly what I needed before tomorrow."
            ),
        ],
    },
    {
        "thread": "Mumbai Office Lease Renewal",
        "messages": [
            (
                "2026-09-21 10:15",
                "Facilities",
                "All",
                "Reminder: the Mumbai office lease renewal requires an authorized signature by Friday, 25 September."
            ),
            (
                "2026-09-22 11:00",
                "Raghav",
                "Arjun, Divya",
                "Following up from the sync — has anyone confirmed who’s signing off on the Mumbai renewal? Don’t think it’s been assigned."
            ),
            (
                "2026-09-23 09:30",
                "Divya",
                "Raghav, Arjun",
                "Not on my end — I believe this typically sits with Facilities directly, not us."
            ),
            (
                "2026-09-24 16:00",
                "Facilities",
                "All",
                "Second reminder: signature is still pending. Deadline is Friday, 25 September, end of day."
            ),
            (
                "2026-09-24 16:45",
                "Raghav",
                "Arjun",
                "This is now one day out and still unowned — can you confirm who’s handling it?"
            ),
        ],
    },
]


VOICE_NOTES = [
    {
        "date": "2026-09-21 18:40",
        "title": "Voice Note 1",
        "text": """
        Quick note to self — need to get Raghav that vendor list, I think I said
        today but it might slip to tomorrow morning, remind me. Also still haven’t
        heard back on the Mumbai lease thing, someone needs to own that, I don’t
        think it’s me.
        """,
    },
    {
        "date": "2026-09-23 08:15",
        "title": "Voice Note 2",
        "text": """
        Reminder — expense variance report from Divya needs to be in my hands by
        Wednesday evening, not Thursday, I want time to go through it before board
        prep. Also Meridian call — I owe Priya a time, need to lock that in today.
        """,
    },
]


CALENDARS = {
    "Arjun": [
        ("2026-09-21", "09:00", "09:35", "Leadership Sync"),
        ("2026-09-21", "14:00", "14:30", "1:1 with Neha"),
        ("2026-09-21", "16:00", "17:00", "Blocked"),
        ("2026-09-22", "11:00", "12:00", "Internal Budget Review"),
        ("2026-09-22", "15:00", "15:30", "Blocked"),
        ("2026-09-23", "15:00", "15:30", "Call — Meridian Logistics"),
        ("2026-09-23", "18:00", "18:15", "Blocked"),
        ("2026-09-24", "09:00", "10:00", "Board Prep Session"),
        ("2026-09-24", "16:00", "17:00", "Hiring Panel — Sales Associate"),
        ("2026-09-25", "10:00", "10:30", "Facilities Check-in"),
        ("2026-09-25", "13:00", "14:00", "Blocked"),
    ],
    "Neha": [
        ("2026-09-21", "10:00", "11:00", "Blocked"),
        ("2026-09-21", "14:00", "14:30", "1:1 with Arjun"),
        ("2026-09-22", "13:00", "14:00", "Campaign Vendor Call"),
        ("2026-09-23", "10:00", "10:30", "Deck Prep"),
        ("2026-09-24", "09:30", "10:00", "Deck Review with Arjun"),
        ("2026-09-25", "11:00", "12:00", "Blocked"),
    ],
    "Raghav": [
        ("2026-09-21", "09:00", "09:35", "Leadership Sync"),
        ("2026-09-21", "13:00", "14:00", "Blocked"),
        ("2026-09-22", "11:00", "12:00", "Internal Budget Review"),
        ("2026-09-22", "15:30", "16:00", "Ops Standup"),
        ("2026-09-23", "09:00", "11:00", "Blocked"),
        ("2026-09-24", "14:00", "15:00", "Blocked"),
        ("2026-09-25", "10:00", "10:30", "Facilities Check-in"),
        ("2026-09-25", "15:00", "16:00", "Blocked"),
    ],
    "Divya": [
        ("2026-09-21", "14:30", "15:00", "Budget Prep"),
        ("2026-09-21", "16:00", "17:00", "Blocked"),
        ("2026-09-22", "09:00", "09:15", "Quick Call with Arjun"),
        ("2026-09-22", "11:00", "12:00", "Internal Budget Review"),
        ("2026-09-23", "13:00", "14:00", "Blocked"),
        ("2026-09-24", "09:00", "10:00", "Board Prep Session"),
        ("2026-09-24", "14:00", "15:00", "Blocked"),
        ("2026-09-25", "10:00", "11:00", "Blocked"),
    ],
}
