from copter.behaviour.Behaviour import Behaviour
from copter.behaviour.RandomDirectionBehaviour import RandomDirectionBehaviour
from geometry.Point import Point

__author__ = 'Martin'


class FleeFromEverythingBehaviour(Behaviour):
    def __init__(self):
        self.no_threat_behaviour = RandomDirectionBehaviour()

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
            return self.no_threat_behaviour.update(current_position, other_copters, obstacles)
        new_position = Point(new_position_x / count,
                             new_position_y / count)
        self.no_threat_behaviour.modifier_x = 1 if new_position.x > current_position.x else -1
        self.no_threat_behaviour.modifier_y = 1 if new_position.y > current_position.y else -1
        return new_position
