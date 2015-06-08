__author__ = 'Martin'


class PointHelper:
    def __init__(self, canvas):
        self.canvas = canvas

    def invert_y(self, y):
        return self.canvas.winfo_height() - y
