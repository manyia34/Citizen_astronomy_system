# milestone_1.py
# Milestone 1 - take input for one observation and print a small report


def viewing_score(visibility_rating, cloud_cover, light_pollution):
    # more visibility = better, more clouds and pollution = worse
    return visibility_rating * 20 - cloud_cover / 5 - light_pollution * 2


def milestone_1():
    print("\n=== MILESTONE 1: Record One Night-Sky Observation ===")

    # taking input from user
    name = input("Observer name : ").strip()
    obj = input("Celestial object : ").strip()
    duration = input("Duration (minutes) : ").strip()
    cloud = input("Cloud cover (%) : ").strip()
    pollution = input("Light pollution (1-5) : ").strip()
    visibility = input("Visibility rating (1-5) : ").strip()

    # input() always gives string, so converting to int / float
    duration = int(duration)
    cloud = float(cloud)
    pollution = int(pollution)
    visibility = int(visibility)

    print("\nType of duration :", type(duration))
    print("Type of visibility :", type(visibility))

    score = viewing_score(visibility, cloud, pollution)

    # using // and % to get hours and minutes
    hrs = duration // 60
    mins = duration % 60

    # code = first 3 letters of name and object
    code = name[:3].upper() + "-" + obj[:3].upper()

    print("\n----- Observation Report -----")
    print("Observer         :", name)
    print("Celestial Object :", obj)
    print("Duration         :", duration, "min =", hrs, "hr", mins, "min")
    print("Cloud Cover      :", str(cloud) + "%")
    print("Light Pollution  :", pollution)
    print("Visibility       :", visibility)
    print("Viewing Score    :", score)
    print("Observation Code :", code)
