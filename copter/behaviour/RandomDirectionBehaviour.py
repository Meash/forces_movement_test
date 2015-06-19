from random import random

from copter.behaviour.Behaviour import Behaviour
from geometry.Point import Point

__author__ = 'Martin'


class RandomDirectionBehaviour(Behaviour):
    def __init__(self):
        self.modifier_x = 1
        self.modifier_y = 1

    def update(self, current_position, other_copters, obstacles):
        self.modifier_x = -1 if random() < 0.5 - self.modifier_x * 0.35 else +1
        self.modifier_y = -1 if random() < 0.5 - self.modifier_y * 0.35 else +1
        return Point(current_position.x + (random() * 10) * self.modifier_x,
                     current_position.y + random() * 10 * self.modifier_y)
