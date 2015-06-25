from math import sqrt
import numbers
from geometry.Entity import Entity

__author__ = 'Martin'


class PointVector(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, PointVector):
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))
        return self.__combine_points(other, lambda a, b: a + b)

    def __sub__(self, other):
        if not isinstance(other, PointVector):
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(self.__class__, type(other)))
        return self.__combine_points(other, lambda a, b: a - b)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return PointVector(self.x * other, self.y * other)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(self.__class__, type(other)))

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return PointVector(self.x / other, self.y / other)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(self.__class__, type(other)))

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def scale(self, scale):
        return self * scale

    def distance(self, p2):
        return sqrt((self.x - p2.x) * (self.x - p2.x)
                    + (self.y - p2.y) * (self.y - p2.y))

    def normal(self):
        length = sqrt(self.x * self.x + self.y * self.y)
        return PointVector(self.x / length, self.y / length)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __combine_points(self, other, func):
        return PointVector(func(self.x, other.x), func(self.y, other.y))

    def get_lib_conversion(self):
        return self.x, self.y

    def __str__(self):
        return "Point[x=" + str(self.x) + ",y=" + str(self.y) + "]"
