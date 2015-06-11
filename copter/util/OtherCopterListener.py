from abc import ABCMeta, abstractmethod

__author__ = 'Martin'


class OtherCopterListener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_other_copters_update(self, other_copters_closest_points):
        pass
