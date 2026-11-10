# milestone_5.py
# Milestone 5 - file handling, exception handling and the full session

import os
import time

from milestones.milestone_1 import viewing_score
from milestones.milestone_2 import CATALOUGE
from milestones.milestone_3 import SkyObservation, MeteorObservation
from milestones.milestone_4 import print_report

LOG_FILE = "night_sky_log.txt"

# milestone 2 catalouge + meteor showers (needed for MeteorObservation)
FULL_CATALOGUE = dict(CATALOUGE)
FULL_CATALOGUE["Perseids"] = "Meteor Shower"
FULL_CATALOGUE["Geminids"] = "Meteor Shower"


# ---------------- saving and reading the log file ----------------

def append_to_log(observations, filename):
    with open(filename, "a") as file:
        for obs in observations:
            file.write(obs.to_log_line() + "\n")


def read_log(filename):
    """Read the log and rebuild objects; skip malformed lines safely.
    Raises FileNotFoundError if the file does not exist (handled by caller)."""
    records = []
    skipped = 0
    with open(filename, "r") as file:
        for line_no, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                parts = line.split(",")
                if len(parts) != 8:
                    raise ValueError(f"expected 8 fields, got {len(parts)}")
                kind, obs_id, observer, obj, cat, dur, rating, meteors = parts
                dur, rating, meteors = int(dur), int(rating), int(meteors)
                if kind == "METEOR":
                    records.append(MeteorObservation(obs_id, observer, obj, cat,
                                                     dur, rating, meteors))
                else:
                    records.append(SkyObservation(obs_id, observer, obj, cat,
                                                  dur, rating))
            except ValueError as error:
                skipped += 1
                print(f"  [SKIPPED] Malformed record at line {line_no}: {line!r} ({error})")
    return records, skipped


def file_size_bytes(filename):
    return os.path.getsize(filename)


# ---------------- taking input with error handling ----------------

def read_int(prompt, low=None, high=None):
    """Read an integer; raise ValueError if it is not a number or out of range."""
    value = int(input(prompt))
    if (low is not None and value < low) or (high is not None and value > high):
        raise ValueError(f"{value} is outside the allowed range {low}-{high}")
    return value


def collect_observations(observer_name):
    observations = []
    counter = 1
    print("Catalogue:", ", ".join(FULL_CATALOGUE))
    print("Type DONE to finish.")
    while True:
        object_name = input("\nObject name (or DONE) : ").strip().title()
        if object_name == "Done":
            break
        if object_name not in FULL_CATALOGUE:
            print(f"  [REJECTED] '{object_name}' is not in the catalogue.")
            continue
        try:   # Milestone 5 (c): ValueError handling
            duration = read_int("Duration (minutes)    : ", 1, 600)
            cloud_cover = read_int("Cloud cover (%)       : ", 0, 100)
            pollution = read_int("Light pollution (1-5) : ", 1, 5)
            rating = read_int("Visibility (1-5)      : ", 1, 5)
            category = FULL_CATALOGUE[object_name]
            obs_id = f"{observer_name[:3].upper()}-{object_name[:3].upper()}-{counter:02d}"
            if category == "Meteor Shower":
                meteors = read_int("Meteor count          : ", 0)
                obs = MeteorObservation(obs_id, observer_name, object_name,
                                        category, duration, rating, meteors)
            else:
                obs = SkyObservation(obs_id, observer_name, object_name,
                                     category, duration, rating)
        except ValueError as error:
            print(f"  [HANDLED] ValueError: {error}. Observation not saved.")
            continue
        observations.append(obs)
        counter += 1
        print(f"  [SAVED] {obs_id} | viewing score = "
              f"{viewing_score(rating, cloud_cover, pollution)}")
    return observations


def show_log():
    """Milestone 5: read valid records, skip malformed ones, show metadata."""
    print(f"\n----------- SAVED LOG: {LOG_FILE} -----------")
    try:
        records, skipped = read_log(LOG_FILE)
    except FileNotFoundError:
        print(f"  [HANDLED] FileNotFoundError: '{LOG_FILE}' does not exist yet.")
        return
    for rec in records:
        print("  ", rec.observation_summary())
    print("\nStored valid records :", len(records))
    print("Malformed skipped    :", skipped)
    print("File size (bytes)    :", file_size_bytes(LOG_FILE))


# ---------------- full session (milestone 4 + 5) ----------------

def full_session():
    print("\n=== MILESTONE 4 + 5: Full Session, Analysis and Log ===")
    observer_name = input("Observer name : ").strip() or "Unknown"
    observations = collect_observations(observer_name)
    # timer starts after input, so it measures only the report generation
    start_time = time.time()
    print_report(observations, start_time)
    if observations:
        append_to_log(observations, LOG_FILE)
        print(f"\n{len(observations)} observation(s) appended to {LOG_FILE}")
        show_log()
    else:
        print("\nNo valid observations - nothing written to the log.")
