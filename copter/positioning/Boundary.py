from geometry.PointVector import PointVector

__author__ = 'Martin'


class Boundary:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_left = PointVector(lower_left.x, upper_right.y)
        self.upper_right = upper_right
        self.lower_right = PointVector(upper_right.x, lower_left.y)
