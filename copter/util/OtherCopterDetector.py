__author__ = 'Martin'


class OtherCopterDetector:
    def __init__(self):
        self.other_copters_listeners = []

    def add_other_copters_listener(self, listener):
        self.other_copters_listeners.append(listener)

    def on_other_copters_update(self, copters_closest_points):
        for listener in self.other_copters_listeners:
            listener.on_other_copters_update(copters_closest_points)
