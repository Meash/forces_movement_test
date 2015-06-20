import sympy

from geometry.Line import Line

__author__ = 'Martin'


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __str__(self):
        return "Circle[center=" + str(self.center) + ",radius=" + str(self.radius) + "]"

    def intersection(self, other):
        sympy_center = sympy.geometry.Point(self.center.x, self.center.y)
        sympy_circle = sympy.geometry.Circle(sympy_center, self.radius)

        if isinstance(other, Circle):
            # use line connection since this circle could overlap with other circle,
            # without intersecting with it
            sympy_other_center = sympy.geometry.Point(other.center.x, other.center.y)
            connection = sympy.geometry.Line(sympy_center, sympy_other_center)
            intersecting_points = connection.intersection(sympy_other_center)
            closest_point = intersecting_points[0]
            if sympy_center.distance(closest_point) <= self.radius:
                return intersecting_points
            return []
        if isinstance(other, Line):
            sympy_other_p1 = sympy.geometry.Point(other.p1.x, other.p1.y)
            sympy_other_p2 = sympy.geometry.Point(other.p2.x, other.p2.y)
            sympy_other_line = sympy.geometry.Line(sympy_other_p1, sympy_other_p2)
            return sympy_circle.intersection(sympy_other_line)

        else:
            raise ValueError("Unhandled type " + other.__class__.__name__)
