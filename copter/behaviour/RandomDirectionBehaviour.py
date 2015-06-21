from random import random

from copter.behaviour.Behaviour import Behaviour
from geometry.PointVector import PointVector

__author__ = 'Martin'


class RandomDirectionBehaviour(Behaviour):
    def __init__(self, acceleration, max_speed):
        self.acceleration = acceleration
        self.max_speed = max_speed
        # range [0, 0.5)
        self.direction_confidence = 0.35

        self.direction_x = 0
        self.direction_y = 0
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self, current_position, other_copters, obstacles):
        self.direction_x = -1 if random() < 0.5 - self.direction_x * self.direction_confidence else +1
        self.direction_y = -1 if random() < 0.5 - self.direction_y * self.direction_confidence else +1

        delta_velocity_x = self.acceleration
        self.velocity_x += delta_velocity_x * self.direction_x
        self.velocity_x = self.assure_range(self.velocity_x)
        delta_velocity_y = self.acceleration
        self.velocity_y += delta_velocity_y * self.direction_y
        self.velocity_y = self.assure_range(self.velocity_y)
        return PointVector(self.velocity_x, self.velocity_y)

    def reset_direction(self, direction_x, direction_y):
        if direction_x not in [-1, 0, 1]:
            raise ValueError("Invalid value {} for direction_x".format(direction_x))
        if direction_y not in [-1, 0, 1]:
            raise ValueError("Invalid value {} for direction_y".format(direction_y))
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction_x = direction_x
        self.direction_y = direction_y

    def assure_range(self, velocity):
        if velocity > self.max_speed:
            return self.max_speed
        if velocity < - self.max_speed:
            return -self.max_speed
        return velocity
