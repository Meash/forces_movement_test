from copter.util.ChangeListener import ChangeListener
from geometry.PointHelper import PointHelper

__author__ = 'Martin'


class CopterDrawer(ChangeListener):
    DRAW_VISION_AREA = False

    def __init__(self, canvas, copter):
        self.canvas = canvas
        self.copter = copter
        self.point_helper = PointHelper(canvas)
        self.drawn_copter = None
        self.drawn_vision_area = None
        self.draw_copter()

    def on_change(self):
        drawn_copter = self.drawn_copter
        drawn_vision_area = self.drawn_vision_area
        self.draw_copter()
        self.canvas.delete(drawn_copter)
        self.canvas.delete(drawn_vision_area)

    def draw_copter(self):
        radius = self.copter.size / 2
        copter_pos = self.copter.position
        x = copter_pos.x
        y = copter_pos.y
        y = self.point_helper.invert_y(y)

        if self.DRAW_VISION_AREA:
            vision_radius = self.copter.sensor.sensor_range
            self.drawn_vision_area = self.canvas.create_oval(
                x - vision_radius, y - vision_radius,
                x + vision_radius, y + vision_radius,
                fill="#9FF781")

        self.drawn_copter = self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius)
