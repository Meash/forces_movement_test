__author__ = 'Martin'


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "Line[p1=" + str(self.p1) + ",p2=" + str(self.p2) + "]"
