from abc import abstractmethod, ABCMeta

__author__ = 'Martin'


class Entity:
    __metaclass__ = ABCMeta

    def intersection(self, other):
        _self = self.get_lib_conversion()
        _other = other.get_lib_conversion()
        return _self.intersection(_other)

    @abstractmethod
    def get_lib_conversion(self):
        pass
