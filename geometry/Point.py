__author__ = 'Martin'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point[x=" + str(self.x) + ",y=" + str(self.y) + "]"
