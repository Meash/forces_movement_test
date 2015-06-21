from math import sqrt
import numbers

from shapely.geometry import LineString

from geometry.Entity import Entity

__author__ = 'Martin'


class Line(Entity):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def len(self):
        a = self.p2.x - self.p1.x
        b = self.p2.y - self.p1.y
        return sqrt(a * a + b * b)

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Line(self.p1 / other, self.p2 / other)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(self.__class__, type(other)))

    def get_lib_conversion(self):
        return LineString([self.p1.get_lib_conversion(), self.p2.get_lib_conversion()])

    def __str__(self):
        return "Line[p1=" + str(self.p1) + ",p2=" + str(self.p2) + "]"
