from sympy.geometry import *
from copter.sensors.Sensor import Sensor

__author__ = 'Martin'


class SensorMock(Sensor):
    def __init__(self, sensor_range, boundary, other_copters):
        self.sensor_range = sensor_range
        self.boundary_lines = self.get_boundary_lines(boundary)
        self.other_copters_circles = self.get_copters_circles(other_copters)

    def collect_obstacles_closest_points(self, position):
        vision_area = Circle(Point(position.x, position.y), self.sensor_range)
        return self.get_closest_points(vision_area, self.boundary_lines)

    def collect_other_copters_closest_points(self, position):
        vision_area = Circle(Point(position.x, position.y), self.sensor_range)
        return self.get_closest_points(vision_area, self.other_copters_circles)

    @staticmethod
    def get_closest_points(vision_area, entities):
        closest_points = []
        for entity in entities:
            intersecting_points = intersection(entity, vision_area)
            if len(intersecting_points) == 1:
                closest_points.append(intersecting_points[0])
            if len(intersecting_points) == 2:
                center = (intersecting_points[0] + intersecting_points[1]) / 2
                closest_points.append(center)
        return closest_points

    @staticmethod
    def get_boundary_lines(boundary):
        ll = boundary.lower_left
        ul = boundary.upper_left
        ur = boundary.upper_right
        lr = boundary.lower_right
        boundary_lines = [Line(Point(ll.x, ll.y),
                               Point(ul.x, ul.y)),
                          Line(Point(ul.x, ul.y),
                               Point(ur.x, ur.y)),
                          Line(Point(ur.x, ur.y),
                               Point(lr.x, lr.y)),
                          Line(Point(lr.x, lr.y),
                               Point(ll.x, ll.y))]
        return boundary_lines

    @staticmethod
    def get_copters_circles(other_copters):
        circles = []
        for copter in other_copters:
            circle = Circle(Point(copter.position.x, copter.position.y),
                            copter.size)
            circles.append(circle)
        return circles
