from shapely.geometry import box

from geometry.Entity import Entity

__author__ = 'Martin'


class Rectangle(Entity):
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def get_lib_conversion(self):
        return box(self.lower_left.x, self.lower_left.y, self.upper_right.x, self.upper_right.y)

    def __str__(self):
        return "Rectangle[ll=" + str(self.lower_left) + ",ur=" + str(self.upper_right) + "]"
