from copter.behaviour.Behaviour import Behaviour
from geometry.PointVector import PointVector

__author__ = 'Martin'


class MoveToTargetFleeBehaviour(Behaviour):
    def __init__(self, target):
        self.target = target

    def update(self, current_position, other_copters, obstacles):
        direction = PointVector(0, 0)
        vectors = []
        target_vec = self.target - current_position
        count = 1
        max_len = target_vec.length()
        vectors.append(target_vec)
        entities = obstacles + other_copters
        for obstacle_point in entities:
            vec = current_position - obstacle_point
            count += 1
            max_len = max(vec.length(), max_len)
            vectors.append(vec)

        for vector in vectors:
            scale = max_len / vector.length()
            direction += vector.scale(scale)

        return direction
