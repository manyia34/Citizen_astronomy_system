# milestone_4.py
# Milestone 4 - analysis functions, lambda mapping and session report

import time

from milestones.milestone_3 import SkyObservation, MeteorObservation


def total_observation_time(observations):
    total = 0
    for obs in observations:
        total += obs.duration_minutes
    return total


def average_visibility(observations):
    # milestone 5 (d) - handling ZeroDivisionError when list is empty
    try:
        total = sum(obs.visibility_rating for obs in observations)
        return total / len(observations)
    except ZeroDivisionError:
        print("  [HANDLED] ZeroDivisionError: no valid observations for average.")
        return 0.0


def session_summary(observations):
    # returns a dictionary with the summary of the whole session
    categories = set()
    meteors = 0
    for obs in observations:
        categories.add(obs.category)
        if isinstance(obs, MeteorObservation):
            meteors += obs.meteor_count

    return {
        "total_observations": len(observations),
        "total_time_minutes": total_observation_time(observations),
        "average_rating": round(average_visibility(observations), 2),
        "unique_categories": sorted(categories),
        "total_meteors": meteors,
    }


def high_quality_observations(observations, minimum_rating=4):
    # minimum_rating is a default parameter
    return [obs for obs in observations if obs.visibility_rating >= minimum_rating]


def is_long_session(obs):
    return obs.duration_minutes >= 60


# name of analysis -> function used for filtering
ANALYSIS_MAP = {
    "HIGH_RATING": lambda obs: obs.visibility_rating >= 4,
    "LONG_SESSION": is_long_session,
    "METEOR_ONLY": lambda obs: isinstance(obs, MeteorObservation),
}


def run_analysis(observations, analysis_name):
    selected_function = ANALYSIS_MAP[analysis_name]
    return list(filter(selected_function, observations))


def print_report(observations, start_time):
    print("\n----- SESSION REPORT -----")
    print("Organization         : ", SkyObservation.organization_name)
    print("Report generated at  : ", time.strftime("%Y-%m-%d %H:%M:%S"))

    summary = session_summary(observations)
    for key, value in summary.items():
        print(f"{key.replace('_', ' ').title():<20}: {value}")

    print("\n All observations : ")
    for obs in sorted(observations, key=lambda o: o.visibility_rating, reverse=True):
        print("  ", obs.observation_summary())

    print("\nHigh quality (default min_rating = 4) : ")
    for obs in high_quality_observations(observations):
        print("  ", obs)

    print("Excellent only (keyword minimum_rating=5):")
    for obs in high_quality_observations(observations, minimum_rating=5):
        print("  ", obs)

    print("\nAnalysis mapping: ")
    for name in ANALYSIS_MAP:
        result = run_analysis(observations, name)
        print(f"  {name:<13} -> {[o.object_name for o in result]}")

    print(f"\nReport generation time: {time.time() - start_time:.4f} seconds")
