# Day 35 - Countdown Timer (2026-11-10)
# What it does: Counts down to any date and time you care about -
# an exam, a flight, Eid, a deadline, a birthday - and shows the
# remaining days, hours, minutes and seconds. It can also run a
# simple live countdown (like a kitchen timer) right in the terminal.
# Useful for: students waiting for exam results, travellers counting
# down to a flight, anyone tracking a deadline or a festival.
# Plain Python - no external libraries needed.

from datetime import datetime, timedelta
import time


def time_until(target, now=None):
    """Return the time left until `target` as a dict.

    `target` can be a datetime, or a string like "2026-12-25 00:00".
    Returns days, hours, minutes, seconds left (all 0 if past).
    """
    if isinstance(target, str):
        target = datetime.strptime(target, "%Y-%m-%d %H:%M")
    now = now or datetime.now()
    delta = target - now
    if delta.total_seconds() <= 0:
        return {"days": 0, "hours": 0, "minutes": 0, "seconds": 0, "passed": True}
    total = int(delta.total_seconds())
    return {
        "days": total // 86400,
        "hours": (total % 86400) // 3600,
        "minutes": (total % 3600) // 60,
        "seconds": total % 60,
        "passed": False,
    }


def format_countdown(target, label="Event"):
    """Return a friendly one-line countdown, e.g. 'Eid: 45 days, 3h 12m left'."""
    left = time_until(target)
    if left["passed"]:
        return f"{label}: time is up!"
    parts = []
    if left["days"]:
        parts.append(f"{left['days']} din")
    if left["hours"]:
        parts.append(f"{left['hours']} ghonta")
    if left["minutes"]:
        parts.append(f"{left['minutes']} minute")
    parts.append(f"{left['seconds']} second")
    return f"{label}: " + ", ".join(parts) + " baki"


def run_timer(seconds, label="Timer"):
    """Run a live terminal countdown for `seconds` seconds, then ring."""
    remaining = int(seconds)
    while remaining > 0:
        mins, secs = divmod(remaining, 60)
        print(f"\r{label}: {mins:02d}:{secs:02d} baki", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print(f"\n{label}: somoy sesh! Ding ding ding!")


if __name__ == "__main__":
    # Example 1: Eid-ul-Fitr er countdown (date bodle nin)
    print(format_countdown("2027-03-20 06:00", "Eid-ul-Fitr"))

    # Example 2: Flight er countdown
    print(format_countdown("2026-12-15 14:30", "Dhaka to Dubai flight"))

    # Example 3: 10-second er live timer (ranna / porar break er jonno)
    run_timer(10, "Chayer timer")
