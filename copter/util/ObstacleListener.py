from abc import ABCMeta, abstractmethod

__author__ = 'Martin'


class ObstacleListener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_obstacles_update(self, obstacles_closest_points):
        pass
