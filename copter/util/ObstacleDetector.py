__author__ = 'Martin'


class ObstacleDetector:
    def __init__(self):
        self.obstacle_listeners = []

    def add_obstacle_listener(self, listener):
        self.obstacle_listeners.append(listener)

    def on_obstacles_update(self, obstacles_closest_points):
        for listener in self.obstacle_listeners:
            listener.on_obstacles_update(obstacles_closest_points)
