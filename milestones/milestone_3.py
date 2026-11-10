# milestone_3.py
# Milestone 3 - parent class SkyObservation, child class MeteorObservation
# and a small demo of inheritance and polymorphism

from milestones.milestone_2 import classify_rating


class SkyObservation:
    # parent class, stores one night sky observation

    organization_name = "Citizen Astronomy Club"

    def __init__(self, observation_id, observer_name, object_name,
                 category, duration_minutes, visibility_rating):
        self.observation_id = observation_id
        self.observer_name = observer_name
        self.object_name = object_name
        self.category = category
        self.duration_minutes = duration_minutes
        self.visibility_rating = visibility_rating

    def quality_label(self):
        return classify_rating(self.visibility_rating)

    def observation_summary(self):
        # one line summary of the observation
        label = self.quality_label()
        summary = f"[{self.observation_id}] {self.object_name} ({self.category}) "
        summary += f"by {self.observer_name} | {self.duration_minutes} min | "
        summary += f"Rating {self.visibility_rating} -> {label}"
        return summary

    def to_log_line(self):
        # meteor count is 0 for normal sky observation
        parts = ["SKY", self.observation_id, self.observer_name, self.object_name,
                 self.category, self.duration_minutes, self.visibility_rating, 0]
        return ",".join(str(p) for p in parts)

    def __str__(self):
        return f"SkyObservation({self.observation_id}, {self.object_name})"


class MeteorObservation(SkyObservation):
    # child class, same as SkyObservation + meteor_count

    def __init__(self, observation_id, observer_name, object_name,
                 category, duration_minutes, visibility_rating, meteor_count):
        # calling the parent constructor
        super().__init__(observation_id, observer_name, object_name,
                         category, duration_minutes, visibility_rating)
        self.meteor_count = meteor_count

    # overriding parent method (polymorphism)
    def observation_summary(self):
        summary = super().observation_summary()
        summary += f" | Meteors: {self.meteor_count}"
        return summary

    def to_log_line(self):
        parts = ["METEOR", self.observation_id, self.observer_name, self.object_name,
                 self.category, self.duration_minutes, self.visibility_rating,
                 self.meteor_count]
        return ",".join(str(p) for p in parts)

    def __str__(self):
        return (f"MeteorObservation({self.observation_id}, {self.object_name}, "
                f"meteors={self.meteor_count})")


def milestone_3():
    print("\n=== MILESTONE 3: Inheritance and Polymorphism ===")
    print("Organization:", SkyObservation.organization_name)

    sky = SkyObservation("OBS-001", "Neha", "Jupiter", "Planet", 95, 4)
    meteor = MeteorObservation("OBS-002", "Neha", "Perseids", "Meteor Shower", 60, 5, 42)

    # same methods called on both objects, output is different (polymorphism)
    for obs in [sky, meteor]:
        print("\n__str__()             :", obs)
        print("quality_label()       :", obs.quality_label())
        print("observation_summary() :", obs.observation_summary())
