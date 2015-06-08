from copter.behaviour.Behaviour import Behaviour
from geometry.Position import Position

__author__ = 'Martin'


class MoveNorthEastBehaviour(Behaviour):
    def __init__(self):
        self.speed = 10

    def update(self, current_position, other_copters, obstacles):
        if len(obstacles) > 0:
            return current_position
        new_position = Position(current_position.x + self.speed, current_position.y + self.speed)
        return new_position
