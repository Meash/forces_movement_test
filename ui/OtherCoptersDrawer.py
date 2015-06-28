from copter.util.OtherCopterListener import OtherCopterListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class OtherCoptersDrawer(OtherCopterListener):
    def __init__(self, copter, canvas):
        self.copter = copter
        self.canvas = canvas
        self.point_helper = PointHelper(canvas)
        self.drawn_copters = []
        self.drawn_connectors = []

    def on_other_copters_update(self, other_copters_closest_points):
        drawn_copters = list(self.drawn_copters)
        drawn_connectors = list(self.drawn_connectors)
        self.draw_copters(other_copters_closest_points)
        for drawn_connector in drawn_connectors:
            self.canvas.delete(drawn_connector)
            self.drawn_connectors.remove(drawn_connector)
        for drawn_copter in drawn_copters:
            self.canvas.delete(drawn_copter)
            self.drawn_copters.remove(drawn_copter)

    def draw_copters(self, other_copters_closest_points):
        size = 5 / 2

        copter_x = self.copter.position.x
        copter_y = self.copter.position.y
        copter_y = self.point_helper.invert_y(copter_y)

        for point in other_copters_closest_points:
            x = point.x
            y = point.y
            y = self.point_helper.invert_y(y)
            drawn_copter = self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill="blue")
            self.drawn_copters.append(drawn_copter)

            drawn_connector = self.canvas.create_line(
                x, y, copter_x, copter_y,
                fill="darkgray"
            )
            self.drawn_connectors.append(drawn_connector)
