__author__ = 'Martin'


class OtherCopterDetector:
    def __init__(self):
        self.other_copter_listeners = []

    def add_other_copter_listener(self, listener):
        self.other_copter_listeners.append(listener)

    def on_other_copters_closest_points_update(self, copters_closest_points):
        for listener in self.other_copter_listeners:
            listener.on_other_copters_closest_points_update(copters_closest_points)
