from copter.behaviour.Behaviour import Behaviour
from geometry.PointVector import PointVector

__author__ = 'Martin'


class FleeFromEverythingBehaviour(Behaviour):
    def __init__(self, no_threat_behaviour):
        self.no_threat_behaviour = no_threat_behaviour

    def update(self, current_position, other_copters, obstacles):
        direction = PointVector(0, 0)
        entities = obstacles + other_copters
        for obstacle_point in entities:
            direction += current_position - obstacle_point

        if len(entities) == 0:
            return self.no_threat_behaviour.update(current_position, other_copters, obstacles)
        self.no_threat_behaviour.reset_direction(direction_x=1 if direction.x > 0 else -1,
                                                 direction_y=1 if direction.y > 0 else -1)
        return direction
