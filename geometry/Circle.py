import shapely.geometry.point

from geometry.Entity import Entity

__author__ = 'Martin'


class Circle(Entity):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle[center=" + str(self.center) + ",radius=" + str(self.radius) + "]"

    def get_lib_conversion(self):
        return shapely.geometry.Point(self.center.x, self.center.y).buffer(self.radius)
