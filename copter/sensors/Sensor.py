from abc import ABCMeta, abstractmethod

__author__ = 'Martin'


class Sensor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def collect_obstacles_closest_points(self, position):
        pass

    @abstractmethod
    def collect_other_copters_closest_points(self, position):
        pass
