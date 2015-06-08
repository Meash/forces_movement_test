from abc import ABCMeta, abstractmethod

__author__ = 'Martin'


class Behaviour:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, current_position, other_copters, obstacles):
        pass
