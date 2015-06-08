__author__ = 'Martin'


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Position[x=" + str(self.x) + ",y=" + str(self.y) + "]"
