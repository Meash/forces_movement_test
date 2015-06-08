__author__ = 'Martin'


class CopterSwarm:
    def __init__(self, copters):
        self.copters = copters

    def change_behaviour(self, behaviour):
        for copter in self.copters:
            copter.set_behaviour(behaviour)
