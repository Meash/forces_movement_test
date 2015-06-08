from abc import ABCMeta, abstractmethod

__author__ = 'Martin'


class ChangeListener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def on_change(self):
        pass
