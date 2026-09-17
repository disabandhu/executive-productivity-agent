# Executive Productivity Agent

A source-grounded executive productivity agent that converts fragmented business inputs into a daily action brief.

Built for Assignment 1 — Executive Productivity Agent.

---

## Problem

Executive commitments are often distributed across meetings, emails, calendars, and personal reminders.

This creates four common problems:

- The same commitment appears in multiple places.
- Deadlines change during conversations.
- It becomes unclear whether the executive or another person owns the next action.
- Important unresolved items can disappear inside long communication threads.

This project converts those fragmented inputs into one canonical action state.

---

## What the Agent Does

The agent:

1. Identifies commitments made by the executive.
2. Separates the executive's actions from dependencies on others.
3. Detects deadlines and overdue commitments.
4. Deduplicates repeated references to the same action.
5. Flags unclear ownership instead of inventing an owner.
6. Produces a daily executive brief.
7. Answers natural-language questions about commitments and actions.
8. Preserves source evidence for traceability.

---

## Architecture

```text
                SOURCE DATA
                     |
        +------------+------------+
        |            |            |
      Meeting      Emails     Calendars
        |            |            |
        +------------+------------+
                     |
                 Voice Notes
                     |
                     v
             +---------------+
             | Normalization |
             +-------+-------+
                     |
                     v
          +----------------------+
          | Commitment Extraction|
          +----------+-----------+
                     |
                     v
          +----------------------+
          | Cross-source          |
          | Deduplication         |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | Ownership Validation  |
          +----------+-----------+
                     |
                     v
          +----------------------+
          | Deadline / State      |
          | Resolution            |
          +----------+-----------+
                     |
                     v
             Canonical Actions
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Daily        Q&A     Traceability
       Brief