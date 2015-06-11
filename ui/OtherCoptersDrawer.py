from copter.util.OtherCopterListener import OtherCopterListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class OtherCoptersDrawer(OtherCopterListener):
    def __init__(self, canvas):
        self.canvas = canvas
        self.point_helper = PointHelper(canvas)
        self.drawn_copters = []

    def on_other_copters_update(self, other_copters_closest_points):
        drawn_copters = list(self.drawn_copters)
        self.draw_copters(other_copters_closest_points)
        for drawn_copter in drawn_copters:
            self.canvas.delete(drawn_copter)

    def draw_copters(self, other_copters_closest_points):
        size = 5 / 2
        for point in other_copters_closest_points:
            # size = point.radius - 0.5
            # point = point.center
            x = point.x.round()
            y = point.y.round()
            y = self.point_helper.invert_y(y)
            drawn_copter = self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill="blue")
            self.drawn_copters.append(drawn_copter)
