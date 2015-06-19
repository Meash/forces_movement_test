from random import random

from copter.behaviour.Behaviour import Behaviour
from geometry.Position import Position

__author__ = 'Martin'


class FleeFromEverythingBehaviour(Behaviour):
    def __init__(self):
        self.modifier_x = 1
        self.modifier_y = 1

    def update(self, current_position, other_copters, obstacles):
        new_position_x = current_position.x
        new_position_y = current_position.y
        count = 1
        for obstacle_point in obstacles:
            vector_hor = obstacle_point.x - current_position.x
            vector_ver = obstacle_point.y - current_position.y
            new_position_x += current_position.x - vector_hor
            new_position_y += current_position.y - vector_ver
            count += 1

        if count == 1:
            self.modifier_x = -1 if random() < 0.5 - self.modifier_x * 0.35 else +1
            self.modifier_y = -1 if random() < 0.5 - self.modifier_y * 0.35 else +1
            return Position(current_position.x + (random() * 10) * self.modifier_x,
                            current_position.y + random() * 10 * self.modifier_y)
        new_position = Position(new_position_x / count,
                                new_position_y / count)
        self.modifier_x = 1 if new_position.x > current_position.x else -1
        self.modifier_y = 1 if new_position.y > current_position.y else -1
        return new_position
