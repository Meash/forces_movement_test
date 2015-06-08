from copter.util.ChangeListener import ChangeListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class CopterDrawer(ChangeListener):
    def __init__(self, canvas, copter):
        self.canvas = canvas
        self.copter = copter
        self.point_helper = PointHelper(canvas)
        self.drawn_copter = None
        self.draw_copter()

    def on_change(self):
        drawn_copter = self.drawn_copter
        self.draw_copter()
        if not (drawn_copter is None):
            self.canvas.delete(drawn_copter)

    def draw_copter(self):
        size_half = self.copter.size / 2
        copter_pos = self.copter.position
        x = copter_pos.x
        y = copter_pos.y
        y = self.point_helper.invert_y(y)
        self.drawn_copter = self.canvas.create_oval(
            x - size_half, y - size_half,
            x + size_half, y + size_half)
