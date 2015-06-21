from copter.util.Changeable import Changeable
from copter.util.ObstacleDetector import ObstacleDetector
from copter.util.OtherCopterDetector import OtherCopterDetector

__author__ = 'Martin'


class Copter(Changeable, ObstacleDetector, OtherCopterDetector):
    def __init__(self, sensor, behaviour, position, boundary, max_speed):
        Changeable.__init__(self)
        ObstacleDetector.__init__(self)
        OtherCopterDetector.__init__(self)
        self.behaviour = behaviour
        self.size = 10
        self.max_speed = max_speed
        self.position = position
        self.boundary = boundary
        self.sensor = sensor

    def update(self):
        other_copters_closest_points, obstacle_closest_points = self.collect_visible_objects()
        super().on_obstacles_update(obstacle_closest_points)
        super().on_other_copters_update(other_copters_closest_points)
        direction = self.behaviour.update(self.position, other_copters_closest_points, obstacle_closest_points)
        distance_len = direction.len()
        if distance_len > self.max_speed:
            direction = direction.scale(self.max_speed / distance_len)
        self.position += direction
        super().on_change()

    def set_behaviour(self, behaviour):
        self.behaviour = behaviour

    def set_sensor(self, sensor):
        self.sensor = sensor

    def collect_visible_objects(self):
        other_copters = self.sensor.collect_other_copters_closest_points(self.position)
        obstacles = self.sensor.collect_obstacles_closest_points(self.position)
        return other_copters, obstacles
