from shapely.geometry import LineString, GeometryCollection, Point

from copter.sensors.Sensor import Sensor
from geometry.Circle import Circle
from geometry.Line import Line
from geometry.PointVector import PointVector

__author__ = 'Martin'


class SensorMock(Sensor):
    def __init__(self, sensor_range, obstacles, other_copters):
        self.sensor_range = sensor_range
        self.obstacles = obstacles
        self.other_copters = other_copters

    def collect_obstacles_closest_points(self, position):
        obstacle_entities = list(map(lambda obstacle: obstacle.geometric_entity, self.obstacles))
        return self.get_closest_points(position, obstacle_entities)

    def collect_other_copters_closest_points(self, position):
        other_copters_circles = self.get_copters_circles(self.other_copters)
        closest_points = []
        for other_copter_circle in other_copters_circles:
            if position.distance(other_copter_circle.center) > self.sensor_range:
                continue
            connection = Line(position, other_copter_circle.center)
            intersection = self.get_closest_point(other_copter_circle, connection)
            if intersection is not None:
                closest_points.append(intersection)
        return closest_points

    def get_closest_points(self, position, entities):
        vision_area = Circle(PointVector(position.x, position.y), self.sensor_range)
        closest_points = []
        for entity in entities:
            closest_point = self.get_closest_point(vision_area, entity)
            if closest_point is not None:
                closest_points.append(closest_point)
        return closest_points

    @staticmethod
    def get_closest_point(circle, other):
        intersection = circle.intersection(other)
        if isinstance(intersection, Point):
            return PointVector(intersection.x, intersection.y)
        if isinstance(intersection, LineString):
            line_coords = intersection.coords
            p1 = line_coords[0]
            if len(line_coords) == 2:
                p2 = line_coords[1]
                points_sum = (p1[0] + p2[0], p1[1] + p2[1])
                result = PointVector(points_sum[0] / 2, points_sum[1] / 2)
                return result
            elif len(line_coords) == 1:
                return PointVector(p1[0], p1[1])
            else:
                raise ValueError("Cannot handle {} line coordinates".format(len(line_coords)))
        if isinstance(intersection, GeometryCollection):
            return None
        else:
            raise ValueError("Unknown type {}".format(intersection.__class__.__name__))

    @staticmethod
    def get_copters_circles(other_copters):
        circles = []
        for copter in other_copters:
            circle = Circle(PointVector(copter.position.x, copter.position.y),
                            copter.size)
            circles.append(circle)
        return circles
