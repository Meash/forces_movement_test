from copter.sensors.Sensor import Sensor
from geometry.Circle import Circle
from geometry.Line import Line
from geometry.Point import Point

__author__ = 'Martin'


class SensorMock(Sensor):
    def __init__(self, sensor_range, boundary, other_copters):
        self.sensor_range = sensor_range
        self.boundary_lines = self.get_boundary_lines(boundary)
        self.other_copters = other_copters

    def collect_obstacles_closest_points(self, position):
        return self.get_closest_points(position, self.boundary_lines)

    def collect_other_copters_closest_points(self, position):
        other_copters_circles = self.get_copters_circles(self.other_copters)
        return self.get_closest_points(position, other_copters_circles)

    def get_closest_points(self, position, entities):
        vision_area = Circle(Point(position.x, position.y), self.sensor_range)
        closest_points = []
        for entity in entities:
            closest_point = self.get_closest_point(vision_area, entity)
            if closest_point is not None:
                closest_points.append(closest_point)
        return closest_points

    @staticmethod
    def get_closest_point(vision_area, entity):
        intersecting_points = vision_area.intersection(entity)
        if len(intersecting_points) == 1:
            return intersecting_points[0]
        elif len(intersecting_points) == 2:
            return (intersecting_points[0] + intersecting_points[1]) / 2
        return None

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
