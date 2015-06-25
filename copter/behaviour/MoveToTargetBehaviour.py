from copter.behaviour.Behaviour import Behaviour

__author__ = 'Martin'


class MoveToTargetBehaviour(Behaviour):
    def __init__(self, target):
        self.target = target

    def update(self, current_position, other_copters, obstacles):
        return self.target - current_position
